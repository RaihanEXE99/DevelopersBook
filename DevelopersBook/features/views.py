from django.shortcuts import render
import asyncio
from django.http import HttpResponse
from .forms import UploadFileForm

import requests, json, time
from io import BytesIO

# Create your views here.
def HtmlEditor(request):
    return render(request, 'features/HtmlEditor.html')
    
def ScreenRecorder(request):
    return render(request,'features/ScreenRecorder.html')

# ace_identifier
def DrawIo(request):
    return render(request, 'features/ProjectCodes.html')

def fileUpload(request):
    if request.method == 'POST':
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                # uploadedFile = request.FILES['file']
                uploadedFile = BytesIO(request.FILES['file'].read())
                uploadedFile.seek(0)
                file = uploadedFile
                files = {'file': open(file, 'rb')}
                url = "https://" + "srv-file7" + ".gofile.io/upload"
                post_response = requests.post(url,filesUploaded=files)


    response = requests.get('https://apiv2.gofile.io/getServer')
    jsonResponse = response.json()
    url = "https://" + jsonResponse['data']['server'] + ".gofile.io/upload"
    print(url)
    form = UploadFileForm()
    return render(request, 'features/fileupload.html', {
        'url': url,
        'form' : form
    })

# def handle_uploaded_file(f):
#     with open('name.mp4', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

# def uploadedFile(request):
#     if request.method == 'POST' and request.FILES['filesUploaded']:
#         myfile = request.FILES['filesUploaded']
#         files = {
#             'filesUploaded': myfile,
#         }
#         response = requests.post('https://srv-file4.gofile.io/upload', files=files)
#         get_response = requests.get('https://srv-file4.gofile.io/upload')
#         jsonResponse = get_response.json()
#         print(get_response)



# files = {
#     'filesUploaded': ('hello.txt', open('hello.txt', 'rb')),
# }

# response = requests.post('https://srv-file6.gofile.io/upload', files=files)
