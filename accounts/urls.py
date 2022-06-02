from .import views
from django.urls import path
urlpatterns = [
    path('',views.loginPage,name='login'),
    path('accounts/signup/', views.signup, name='signup'),

]