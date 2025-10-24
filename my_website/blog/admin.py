from django.contrib import admin
from .models import Post # Import your Post model

# Register your models here.
# This tells Django to show the Post model in the admin site
admin.site.register(Post) 

