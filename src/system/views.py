
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import pandas as pd

som = pd.read_csv('system/image_som_result20230107_121146.csv', index_col=0)
list_som = []
for i in som.index:
    list_som.append(i)

title_som = pd.read_csv('system/title_som_result.csv', index_col=0)
list_title = []
for i in title_som.index:
    list_title.append(i)

represent_image = pd.read_csv('system/rep_image_som_result20230108_170422.csv', index_col=0)
rep_image = []
for i in represent_image.index:
    rep_image.append(i)

image_title = pd.read_csv('system/imageName_title_rename_dict.csv', index_col=0).to_dict()
links = pd.read_csv('system/imageName_link_rename_dict.csv', index_col=0).to_dict()
title_image = pd.read_csv('system/title_imageName_rename_dict.csv', index_col=0).to_dict()


@xframe_options_exempt
# Create your views here.
def electionView(request):
    ctx = {}
    ctx["rep_image"] = rep_image
    ctx["image_title"] = image_title['col2']
    ctx["links"] = links['col2']
    return render(request, 'system/elections.html', ctx)

def imgSOMView(request):
    ctx = {}
    ctx["links"] = links['col2']
    if "id" in request.GET:
        ctx = request.GET
    return render(request, 'system/img-som.html', ctx)

def SOM(request):
    ctx = {}
    ctx["image_title"] = image_title['col2']
    ctx["links"] = links['col2']
    ctx["image_som"] = list_som
    return render(request, 'system/som.html', ctx)

def menu(request):
    return render(request, 'system/menu.html')

def titleSOMView(request):
    ctx = {}
    ctx["image_title"] = image_title['col2']
    ctx["links"] = links['col2']
    ctx["title_som"] = list_title
    ctx["title_image"] = title_image['col2']
    return render(request, 'system/title-som.html', ctx)

def getPost(request):
    ctx = {}
    ctx["id"] = request.POST["id"]
    return(request, '', ctx)