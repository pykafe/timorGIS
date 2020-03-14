from django.urls import path
from .views import MapView, AnotherView, AddPostView

urlpatterns = [
    path('', MapView.as_view()),
    path('another', AnotherView.as_view()),
    path('new/', AddPostView.as_view(), name='new_post'),
]
