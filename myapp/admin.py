from django.contrib import admin
from .models import Blog
from .models import Media
# Register your models here.


admin.site.register(Blog)
admin.site.register(Media)

class Admin(admin.ModelAdmin):
    list_display = ['blog_entry']
