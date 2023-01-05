from django.urls import path
from .views import electionView, imgSOMView, SOM, menu, titleSOMView


urlpatterns = [
    path('election/', electionView),
    path('', imgSOMView),
    path('som.html/', SOM, name="img-som-frame"),
    path('menu.html/', menu, name="menu"),
    path('title.html/', titleSOMView, name="title-som-frame")
]
