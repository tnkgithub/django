
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import pandas as pd

som = pd.read_csv('/home/b1019035/django/src/system/image_som_result.csv', index_col=0)
list_som = []
for i in som.index:
    list_som.append(i)
title = pd.read_csv('/home/b1019035/django/src/system/imageName_title_rename_dict.csv', index_col=0).to_dict()
links = pd.read_csv('/home/b1019035/django/src/system/imageName_link_rename_dict.csv', index_col=0).to_dict()

@xframe_options_exempt
# Create your views here.
def electionView(request):
    return render(request, 'system/elections.html')

def imgSOMView(request):
    return render(request, 'system/img-som.html')

def SOM(request):
    ctx = {}
    ctx["title"] = title['col2']
    ctx["links"] = links['col2']
    ctx["som"] = list_som
    ctx["example"] = {'a.a':'a.a'}
    return render(request, 'system/som.html', ctx)

def menu(request):
    return render(request, 'system/menu.html')

def titleSOMView(request):
    return render(request, 'system/title-som.html')