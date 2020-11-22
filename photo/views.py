from django.shortcuts import render
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile

# Create your views here.
def instagram(request):
    return render(request, 'instagram.html')

def photo(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('home')

    else:
        
        profile_form = ProfileUpdateForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        context = {
            'user_form':user_form,
            'profile_form': profile_form

        }
    return render(request, 'all-photo/photo.html', context)

def search_profile(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photo/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photo/search.html',{"message":message})


