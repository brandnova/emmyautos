from django.db import models

class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=100, default='My Website')
    logo = models.ImageField(upload_to='logos/', default='')
    hero = models.ImageField(upload_to='heros/', default='')
    hero_title = models.CharField(max_length=100, default='Welcome to My Website')
    hero_subtitle = models.CharField(max_length=100, default='Discover our amazing services')
    about = models.ImageField(upload_to='abouts/', default='')
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    phone2 = models.CharField(max_length=20, null=True, blank=True, default='')
    address = models.CharField(max_length=100, null=True, blank=True)
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.site_name

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')
    def __str__(self):
        return self.name 

class SocialMediaLink(models.Model):
    SOCIAL_MEDIA_CHOICES = [
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('telegram', 'Telegram'),
    ]

    platform = models.CharField(max_length=50, choices=SOCIAL_MEDIA_CHOICES)
    url = models.URLField()

    def __str__(self):
        return self.platform



class Review(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='review_photos/')
    def __str__(self):
        return self.name 
    

class Booking(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=12)
    description=models.TextField()

    def __str__(self) : 
        return f'Message from {self.name}'
    
class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery_photos/')
   

class Contact(models.Model):
    name=models.CharField(max_length=30, null= True)
    email=models.EmailField(null= True)
    phoneNumber=models.CharField(max_length=12, null= True)
    description=models.TextField(null= True)

    def __str__(self) : 
        return f'Message from {self.name}'

class Brand(models.Model):
    logo = models.ImageField(upload_to='brands', null=True, blank=True)

    def __str__(self):
        return f"Brand Logo"