from django.urls import path
from .views import languagesListviews,DetailsListviews

urlpatterns = [
    path('', languagesListviews.as_view(), name='language_list'),
    path('<int:pk>',DetailsListviews.as_view(),name='language_detail')
]