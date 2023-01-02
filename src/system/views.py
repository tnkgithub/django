from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import pandas as pd


df_imageSOM_result = pd.read_csv('/home/b1019035/python/gra_study/result_image_SOM20221225_230246.csv', index_col=0)
list_imageSOM_result = df_imageSOM_result.to_numpy().tolist()

img_title = []
img_title = sum(list_imageSOM_result, [])

@xframe_options_exempt
# Create your views here.
def electionView(request):
    return render(request, 'system/elections.html')

def imgSOMView(request):
    return render(request, 'system/img-som.html')

def SOM(request):
    ctx = {}
    ctx["som_image_list"] = img_title
    return render(request, 'system/som.html', ctx)

def menu(request):
    return render(request, 'system/menu.html')

def titleSOMView(request):
    return render(request, 'system/title-som.html')