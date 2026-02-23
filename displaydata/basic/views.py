from django.shortcuts import render,redirect
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import time
current_cmd = 'S'
def set_command(request):
    global current_cmd
    if request.method =='POST':
        current_cmd = request.POST.get('command')
        print(current_cmd)
    return redirect('data')
@csrf_exempt
def showdata(request):
    temp = None
    if request.method=='POST':
        data = json.loads(request.body)

        temp = data.get('temperature')
        
        print("temp", temp)
    if request.method == 'GET':
        return JsonResponse({"cmd": current_cmd})

    return render(request,'show.html',{"temp":temp})



def upload_image(request):
    if request.method =='POST':
        image = request.body
        filename = f"esp32_{int(time.time())}.jpg"
        with open(filename,"wb") as f:
            f.write(image)

        return JsonResponse({"status": "saved"})

    return JsonResponse({"error": "Invalid request"})