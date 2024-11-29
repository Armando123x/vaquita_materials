from django.urls import path
from admin_material import views
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/',permanent=True), name='index'),
    path('billing/', RedirectView.as_view(url='/',permanent=True), name='billing'),
    path('tables/', RedirectView.as_view(url='/',permanent=True), name='tables'),
    path('vr/', RedirectView.as_view(url='/',permanent=True),name='vr'),
    path('rtl/', RedirectView.as_view(url='/',permanent=True), name='rtl'),#no es necesario
    path('notification/', RedirectView.as_view(url='/',permanent=True),name='notification'),
    path('profile/', RedirectView.as_view(url='/',permanent=True), name='profile'), #No es necesario 

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/',LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('accounts/register/', RedirectView.as_view(url='/',permanent=True), name='register'), #Se redirige por motivos de seguridad
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done"),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
