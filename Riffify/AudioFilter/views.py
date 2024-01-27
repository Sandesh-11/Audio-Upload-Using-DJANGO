from django.shortcuts import render,HttpResponse,redirect
from .forms import AudioFileForm


def index(request):
    return render (request,'Homepage.html')

def upload(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Success!!!') 
    else:
        form = AudioFileForm()

    return render(request, 'audio.html', {'form': form})



