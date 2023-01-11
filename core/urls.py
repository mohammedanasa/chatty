from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.frontpage, name="front-page"),
    path('signup/', views.signup, name="signup"),
    path('signin/', auth_views.LoginView.as_view(template_name='core/signin.html'), name="signin"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout")
]
