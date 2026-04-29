from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, editar_perfil 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', register, name='Signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='Login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='Logout'),
    path('profile/edit/', editar_perfil, name='EditarPerfil'),
    path('password/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html', 
        success_url='/accounts/login/'), name='CambiarPassword'),
]

