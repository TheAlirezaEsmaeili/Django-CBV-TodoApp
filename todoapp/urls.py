from django.urls import path,include
from .views import todoListView

urlpatterns = [
    path('',todoListView.as_view(),name='todotask'),
]