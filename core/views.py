from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render
from .models import SiteConfiguration, TeamMember, SocialMediaLink, Contact, Review, Booking, Gallery, Brand
from django.contrib import messages

def home(request):
    site_config = SiteConfiguration.objects.first()
    brands = Brand.objects.all()
    team_members = TeamMember.objects.all()
    reviews = Review.objects.all()
    gallery_images = Gallery.objects.all()
    social_links = SocialMediaLink.objects.all()
    contact_info = Contact.objects.first()
    return render(request, 'core/home.html', {
        'site_config': site_config,
        'team_members': team_members,
        'brands': brands,
        'social_links': social_links,
        'contact_info': contact_info,
        'reviews': reviews,
        'gallery_images': gallery_images 
    })

def about(request):
    site_config = SiteConfiguration.objects.first()
    contact_info = Contact.objects.first()

    return render(request, 'core/about.html', {'site_config': site_config, 'contact_info': contact_info  })


def booking(request):
    site_config = SiteConfiguration.objects.first()
    contact_info = Contact.objects.first()
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        query = Booking(name=fname, email=femail, phoneNumber=phone, description=description)
        query.save()
        messages.info(request, "Thanks For Reaching Us! We will get back to you soon....")
        return redirect('/booking')
    return render(request, 'core/booking.html', {'site_config': site_config, 'contact_info': contact_info})


def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        phone = request.POST.get('phone')
        description= request.POST.get('description')
        query=Contact(name=fname,email=femail,phoneNumber=phone,description=description)
        query.save()
        messages.info(request,"Thanks For Reaching Us! We will get back to you soon....")
        return redirect('/contact')
    return render(request, 'core/home.html', {})

