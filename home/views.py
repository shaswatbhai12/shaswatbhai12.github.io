from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CarouselImage, Product, Testimonial, ProductImage, Contact,WhyChooseUs
from .forms import ContactForm, QuickEnquiryForm  # ✅ Fixed import

# Home Page View
def home(request):
    carousel_images = CarouselImage.objects.all()
    products = Product.objects.all()
    testimonials = Testimonial.objects.all()  # Fetch testimonials
    why_choose_us = WhyChooseUs.objects.all()  # Ensure this line is fetching data

    return render(request, 'home/index.html', {
        'carousel_images': carousel_images,
        'products': products,
        'testimonials': testimonials,
        'why_choose_us': why_choose_us  # ✅ Corrected variable name
    })



# Product Detail View
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_images = ProductImage.objects.filter(product=product)  # Fetch all sub-products (images)

    return render(request, 'home/product_detail.html', {
        'product': product,
        'product_images': product_images,
    })


# Sub-Product Detail View
def sub_product_detail(request, image_id):
    sub_product = get_object_or_404(ProductImage, id=image_id)  # Get clicked sub-product
    product = sub_product.product  # Get parent product
    related_images = ProductImage.objects.filter(product=product)  # Fetch related images

    return render(request, 'home/sub_product_detail.html', {
        'sub_product': sub_product,
        'related_images': related_images,
    })


# Contact Form View
def contact_view(request):
    product_id = request.GET.get("product")  # Use GET instead of POST
    sub_product_id = request.GET.get("sub_product")

    product = Product.objects.filter(id=product_id).first()
    sub_product = ProductImage.objects.filter(id=sub_product_id).first()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.product = product  # Assign product object
            contact.sub_product_name = sub_product.description if sub_product else None
            contact.save()

            messages.success(request, "Your inquiry has been submitted successfully!")
            return redirect("thank_you_page")
        else:
            messages.error(request, "There was an error in your submission. Please check your input.")
    else:
        form = ContactForm()

    return render(request, "home/contact.html", {
        "form": form,
        "product_name": product.name if product else "Unknown Product",
        "sub_product_name": sub_product.description if sub_product else None,
    })



# Quick Enquiry Form View
from django.shortcuts import render, redirect
from .forms import QuickEnquiryForm

def quick_enquiry(request):
    if request.method == 'POST':
        form = QuickEnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you_page')
        else:
            print(form.errors)  # Print errors to debug
            return render(request, 'quick_enquiry.html', {'form': form})  # Show form errors
    else:
        form = QuickEnquiryForm()
    
    return render(request, 'quick_enquiry.html', {'form': form})




# Thank You Page View
def thank_you_page(request):
    return render(request, "home/thank_you.html")


# Static Pages
def about(request):
    return render(request, "home/about.html")

from django.shortcuts import render
from .models import Service

def services(request):
    services_list = Service.objects.all()
    return render(request, "home/services.html", {"services": services_list})


from django.shortcuts import render
from .models import GalleryItem

def gallery(request):
    gallery_items = GalleryItem.objects.all()
    media_type = request.GET.get("type")
    if media_type:
        gallery_items = GalleryItem.objects.filter(media_type=media_type)
    else:
        gallery_items = GalleryItem.objects.all()

    return render(request, "home/gallery.html", {"gallery_items": gallery_items})


def contact_us(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
           
            contact.save()

            messages.success(request, "Your inquiry has been submitted successfully!")
            return redirect("thank_you_page")
        else:
            messages.error(request, "There was an error in your submission. Please check your input.")
    else:
        form = ContactForm()

    return render(request, "home/contact_us.html", {
        "form": form,

    })


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import Subscription

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not Subscription.objects.filter(email=email).exists():
                form.save()
                messages.success(request, "Thank you for subscribing!")
            else:
                messages.warning(request, "You are already subscribed!")
        else:
            messages.error(request, "Invalid email address.")
        return redirect('home')

    return redirect('home')
