from django.contrib import admin
from .models import Artikel

# Register your models here agar tampil pada dashboard.

class ArtikelAdmin(admin.ModelAdmin):
    # Menampilkan model yang di set tidak bisa diedit pada dashboard
    readonly_fields=[
        'slug','published','updated'
    ]

admin.site.register(Artikel,ArtikelAdmin)