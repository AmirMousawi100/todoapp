from django.contrib import admin
from .models import Books

# Register your models here.


admin.site.register(Books)


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",),
    }
