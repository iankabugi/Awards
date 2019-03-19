from django.contrib import admin
from .models import Profile, Project, DesignRating, ContentRating, UsabilityRating

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(DesignRating)
admin.site.register(ContentRating)
admin.site.register(UsabilityRating)
