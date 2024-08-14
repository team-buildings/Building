from django.contrib import admin
from django.utils.html import format_html
from .models import Location, Buildings, Floor, Home, News, Clients
from .forms import ClientsForm

# Register your models here.
admin.site.register(Location)
admin.site.register(Buildings)
admin.site.register(Floor)
admin.site.register(Home)
admin.site.register(News)

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    form = ClientsForm
    list_display = ("fish", "telefon", "term", "home", "oylik_tolov", "colored_status", "custom_button")

    def custom_button(self, obj):
        if obj.status == '1':
            return format_html(
                '<a class="button" href="{}" target="_blank">Shartnoma</a>', f"/contract"
            )
        return format_html('<span></span>')

    custom_button.short_description = "Action"  # Tugma ustida ko'rinadigan sarlavha
    
    def colored_status(self, obj):
        if obj.status == '1':
            color = 'yellow'
        elif obj.status == '0':
            color = 'red'
        elif obj.status == '2':
            color = 'green'
        else:
            color = 'black'
        
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            obj.get_status_display()
        )
    
    colored_status.short_description = 'Status'
