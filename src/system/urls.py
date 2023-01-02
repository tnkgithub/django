from django.urls import path
from .views import electionView, imgSOMView, SOM, menu


urlpatterns = [
    #path('', electionView),
    path('', imgSOMView),
    path('som.html/', SOM),
    path('menu.html/', menu)
]
