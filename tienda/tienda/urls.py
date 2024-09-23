from django.contrib import admin
from django.urls import path
from empanadas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empanadas/', views.empanadas),
]
