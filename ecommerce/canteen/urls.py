from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

