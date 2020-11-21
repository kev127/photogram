from django.shortcuts import render

# Create your views here.
def instagram(request):
    return render(request, 'instagram.html')

def photo(request):
    return render(request, 'all-photo/photo.html')


