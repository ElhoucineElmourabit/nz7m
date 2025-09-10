from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

from supabase import create_client
from django.conf import settings
import uuid

from django.shortcuts import get_object_or_404

url = settings.SUPABASE_URL
key = settings.SUPABASE_KEY
bucket = settings.SUPABASE_BUCKET
supabase = create_client(url, key)


def customer_list(request):
    context = {'customer_list': Customer.objects.all()}
    return render(request, "customer_register/customer_list.html", context)

def customer_form(request, id=0):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save(commit=False)

            file = request.FILES.get('upload_photo')  
            if file:
                ext = file.name.split('.')[-1]
                unique_name = f"{uuid.uuid4()}.{ext}"
                file_path = f"customers/{unique_name}"

                supabase.storage.from_(bucket).upload(
                    file_path,
                    file.read(),
                    {"upsert": "true"}   
                )

                public_url = supabase.storage.from_(bucket).get_public_url(file_path)
                customer.request_photo = public_url


            customer.save()
            return redirect('/customer/list')
    else:
        if id==0:
            form = CustomerForm()
        else:
            form = CustomerForm(Customer.objects.get(pk=id))

    return render(request, "customer_register/customer_form.html", {"form": form})

def customer_delete(request):
    return

def toggle_order_finished(request, id):
    customer = get_object_or_404(Customer, pk=id)
    customer.order_finished = not customer.order_finished  # switch True/False
    customer.save()
    return redirect('/customer/list')