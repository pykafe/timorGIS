from django.urls import path
from .views import MapView, AnotherView, AddUserView

urlpatterns = [
    path('', MapView.as_view()),
    path('another', AnotherView.as_view()),
    path('add_user', AddUserView.as_view(), name='add_user'),
]
