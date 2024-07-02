from django.urls import path
from . import views
from .views import logout_view

app_name="accountapp"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name="logout"),
]