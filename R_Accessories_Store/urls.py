
from django.contrib import admin
from django.urls import path

from home import views # Import the views from the home app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.my_view, name= 'home'),  # Add a URL pattern for the home view

]