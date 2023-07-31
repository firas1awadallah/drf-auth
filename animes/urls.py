from django.urls import path

from .views import AnimelistView,AnimeDetailView
urlpatterns = [
   
   path('',AnimelistView.as_view(), name= 'anime_list'),
   path('<int:pk>/',AnimeDetailView.as_view(), name= 'anime_detail')

]