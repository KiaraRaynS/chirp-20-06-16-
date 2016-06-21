from django.contrib import admin
from appdjango.models import Chirp


class ChirpAdmin(admin.ModelAdmin):
    list_display = ['body', 'user']
    search_fields = ['body']
    # Will impliment a search bar

admin.site.register(Chirp, ChirpAdmin)
