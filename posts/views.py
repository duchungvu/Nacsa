from django.shortcuts import render
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Post, UserProfile

# Create your views here.
def index(request):
    return render(request,
                'base.html',
                {'userprofile' : UserProfile.objects.all()})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request,
                'users/register.html',
                {'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'users/login.html')

class PostView(generic.DetailView):
    model = Post
    template_name = "posts/post.html"

class PostListView(generic.ListView):
    template_name = 'posts/postlist.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()

class ProfileView(generic.ListView):
    model = UserProfile
    template_name = "posts/profile.html"

    def get_queryset(self):
        return UserProfile.objects.all()




