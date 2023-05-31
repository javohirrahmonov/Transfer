from django.contrib import admin
from .models import *
@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('id','player','eski','yangi')
    list_filter = ('mavsum',)
    autocomplete_fields = ('eski','yangi','player')


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display=('id','nom', 'davlat')
    list_display_links = ("nom",)
    search_fields = ('nom',)
    search_help_text = 'Nomi boyicha qidiring !'
    list_filter = ("davlat",)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('ism','club','t_yil','tr_narx','davlat')
    list_display_links = ('ism',)
    search_fields = ('ism',)
    search_help_text = 'Ismi boyicha qidiring!'
    list_filter = ('club',)
    autocomplete_fields = ('club',)

# admin.site.register(Transfer),
admin.site.register(HozirgiMavsum),
# admin.site.register(Player),

