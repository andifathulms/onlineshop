from django.urls import path

from account.views import(
	login_check,
    register_check
) 

app_name = 'account'

urlpatterns = [
	path('login_check/', login_check, name="login-check"),
    path('register_check/', register_check, name="register-check"),
]