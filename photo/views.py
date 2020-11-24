from django.shortcuts import render
from .forms import UserUpdateForm, ProfileUpdateForm ,NewPostForm
from .models import Profile, Post
from .forms import SignUpForm, NewPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from cloudinary.forms import cl_init_js_callbacks      
from .forms import ImageForm

# Create your views here.
def landing(request):
    posts = Post.all_posts()
    json_posts = []
    for post in posts:

        # import pdb; pdb.set_trace()
        pic = Profile.objects.filter(user=post.user.id).first()
        if pic:
            pic = pic.profile_pic.url
        else:
            pic =''
        obj = dict(
            author=post.user.username,
            avatar=post.profile_pic,
            name=post.title,
            caption=post.caption

        )
        json_posts.append(obj)
    return render(request, 'all-photo/landing.html', {"posts": json_posts})

@login_required(login_url='/accounts/login/')
def login(request):
    posts = Post.all_posts()
    json_posts = []
    for post in posts:

        # import pdb; pdb.set_trace()
        pic = Profile.objects.filter(user=post.user.id).first()
        if pic:
            pic = pic.profile_pic.url
        else:
            pic =''
        obj = dict(
            author=post.user.username,
            avatar=post.profile_pic,
            name=post.title,
            caption=post.caption

        )
        json_posts.append(obj)
    return render(request, 'all-photo/landing.html', {"posts": json_posts})

def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        
        profile_form = ProfileUpdateForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        context = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'all-photo/profile.html', {'user_form':user_form,'profile_form':profile_form})

def search_profile(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photo/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photo/search.html',{"message":message})

def new_post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
           
            image.save()
            


    else:
        form = NewPostForm()
    return render(request, 'all-photo/new_post.html', {"form": form})
    
def update_profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

    return render(request, 'all-photo/profile.html', {'user_form':user_form,'profile_form':profile_form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

def upload(request):
  context = dict( backend_form = ImageForm())

  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'all-photo/landing.html', context)


