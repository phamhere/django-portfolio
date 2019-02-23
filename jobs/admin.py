from django.contrib import admin

# Register models and registers them to admin site
from .models import Jobs

admin.site.register(Jobs)
