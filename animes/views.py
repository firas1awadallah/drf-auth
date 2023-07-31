from django.shortcuts import render
from .models import Anime
from django.shortcuts import render
from .models import Anime
from .serializers import AnimeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .permissions import OwnerOnly

class AnimelistView(ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class AnimeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes =[OwnerOnly]