from django.contrib import admin
from appdjango.models import Chirp, StopWord, Profile


class StopWordAdmin(admin.ModelAdmin):
    list_display = ['word']
    search_fields = ['word']

admin.site.register(StopWord, StopWordAdmin)


class ChirpAdmin(admin.ModelAdmin):
    list_display = ['body', 'user']
    search_fields = ['body']
    # Will impliment a search bar

admin.site.register(Chirp, ChirpAdmin)


admin.site.register(Profile)
