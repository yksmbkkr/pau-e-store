from django.urls import path
from coreapp import views

app_name='coreapp'

urlpatterns = [
    path('browser-auth/', views.browser_auth, name='browser-auth'),
    path('app-logout/', views.app_logout, name='app-logout')
]