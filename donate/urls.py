from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "MEDICINE DONATION PORTAL"
admin.site.site_title = "Welcome to the Medicine Donation database"
admin.site.index_title = "Welcome to the Medicine Donation database"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))

]
