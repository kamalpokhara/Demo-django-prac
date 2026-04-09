from django.shortcuts import redirect, render

from project import settings
from .models import Donation
from django.contrib import messages
from django_esewa import EsewaPayment
import uuid
from django.conf import settings
import requests


# Create your views here.
def donate(req):
    if req.method == "POST":
        donor = req.POST.get("donor")
        email = req.POST.get("email")
        amount = req.POST.get("amount")
        uid = uuid.uuid4()

        donation = Donation.objects.create(
            uuid = uid,
            donor=donor, 
            email=email, 
            amount=amount, 
            total_amount=amount
            )
        messages.success(req, "Donation created successfully!")
        return redirect("donations:donation_confirm", uuid=donation.uuid)

    return render(req, "donations/donate.html")

def confirm(req,uuid):
    order = Donation.objects.get(uuid=uuid)
    payment = EsewaPayment(
        product_code= order.product_code,
        success_url= f"http://localhost:8000/donations/success/{order.uuid}/",
        failure_url= f"http://localhost:8000/donations/failure/{order.uuid}/",
        amount=order.amount,
        tax_amount=order.tax_amount,
        total_amount=order.total_amount,
        product_delivery_charge=order.delivery_charge,
        product_service_charge=order.service_charge,
        transaction_uuid=order.uuid,
        secret_key='8gBm/:&EnhH.1/q',
    )
    signature = payment.create_signature() #Saves the signature as well as return it
 
    context = {
        'form':payment.generate_form(),
        'order': order,
    }

    return render(req, "donations/confirm.html",context)

def success(req, uuid):
    object = Donation.objects.get(uuid=uuid)
    object.confirmed = True
    object.save()

    return render(req, "donations/success.html")    

def failure(req, uuid):

    return render(req, "donations/failure.html")


def khalti_confirm(req, uuid):
    order = Donation.objects.get(uuid=uuid)

    payload = {
        "return_url": f"http://127.0.0.1:8000/donations/khalti/verify/{order.uuid}/",
        "website_url": "http://127.0.0.1:8000/",
        "amount": int(order.total_amount) * 100,  # Khalti expects paisa
        "purchase_order_id": str(order.uuid),
        "purchase_order_name": "Donation",

    }
    headers = {"Authorization": f"Key {settings.KHALTI_SECRET_KEY}"}
    res = requests.post(
        f"{settings.KHALTI_GATEWAY_URL}epayment/initiate/", json=payload, headers=headers
    )  # <-- use requests.post
    print(res.text)

    data = res.json()

    return redirect(data["payment_url"])


def khalti_verify(req, uuid):
    order = Donation.objects.get(uuid=uuid)

    pidx = req.GET.get("pidx")
    headers = {
        "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
        # "Content-Type": "application/json",
    }
    res = requests.post(
        f"{settings.KHALTI_VERIFY_URL}",
        json={"pidx": pidx},
        headers=headers,
    )
    print(res.text)
    data = res.json()

    if data.get("status") == "Completed":
        order.confirmed = True
        order.save()
        return render(req, "donations/success.html", {"order": order})
    return render(req, "donations/failure.html", {"order": order})
