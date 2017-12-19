from django.conf.urls import url
from .views import UserListView

urlpatterns = [
    url(r'^users/', UserListView.as_view(), name='user-list')
]
