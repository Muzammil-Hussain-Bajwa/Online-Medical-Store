from django.contrib import admin
from django.urls import path
from django.conf.urls import include

admin.site.site_header = "BAJWA HOMEOPATHIC Admin"
admin.site.site_title = "BAJWA HOMEOPATHIC Portal"
admin.site.index_title = "Welcome to BAJWA HOMEOPATHIC"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
