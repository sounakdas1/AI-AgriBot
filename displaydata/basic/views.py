from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def showdata(request):
    temp = None
    if request.method=='POST':
        data = json.loads(request.body)

        temp = data.get('temperature')

        print("temp", temp)
    return render(request,'show.html',{"temp":temp})