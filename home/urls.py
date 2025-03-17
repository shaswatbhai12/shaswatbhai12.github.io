from django.urls import path
from .views import home, contact_view, quick_enquiry, product_detail, sub_product_detail, about, services, thank_you_page, gallery,contact_us, subscribe

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact_view, name="contact"),
    path("quick-enquiry/", quick_enquiry, name="quick_enquiry"),
    path("product/<int:product_id>/", product_detail, name="product_detail"),
    path("sub-product/<int:image_id>/", sub_product_detail, name="sub_product_detail"),
    path("about/", about, name="about"),
    path("services/", services, name="services"),
    path("gallery/", gallery, name="gallery"),
    path("thank-you/", thank_you_page, name="thank_you_page"),
    path("contact_us/", contact_us, name="contact_us"),
    path('subscribe/', subscribe, name='subscribe'),

]

