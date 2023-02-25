from django.contrib import admin
from .models import Registration, Login, Entry, Restaurant
# Register your models here.
# user login:manan@12 and pw:adman234

admin.site.register(Registration)

admin.site.register(Login)

admin.site.site_header = 'Asset Management'

# admin.site.register(Restaurant, RestaurantAdmin)
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['Date_of_Purchase','No_of_Dishes', 'No_of_Spoon', 'Water_bottles', 'No_of_Fans'] 
    search_fields = ['No_of_Dishes']

# admin.site.register(Entry)
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['assetname','assetserialNo', 'assetmanufacturer','dropdown'] 
    search_fields = ['assetname']