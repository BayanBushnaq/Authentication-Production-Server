from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import LanguageSerializer
from .models import Language
from .permissions import OwnerOnly
# Create your views here.

class languagesListviews(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class DetailsListviews(RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes=[OwnerOnly]

