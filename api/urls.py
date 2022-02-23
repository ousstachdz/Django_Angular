from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import  UserDetail, MessageDetail

urlpatterns =[
        path('profil/', UserDetail.as_view()),
        path('message/', MessageDetail.as_view()),
        # path('profile/', UserAPI.as_view()),
]


# urlpatterns = format_suffix_patterns(urlpatterns)