from django.contrib import admin
from .models import SiteConfiguration, TeamMember, SocialMediaLink, Review, Booking, Gallery, Contact, Brand

admin.site.register(SiteConfiguration)
admin.site.register(TeamMember)
admin.site.register(SocialMediaLink)
admin.site.register(Contact)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(Gallery)