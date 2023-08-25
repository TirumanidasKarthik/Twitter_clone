from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


from .models import Profile, Tweet
from .forms import TweetForm, SignupForm, UpdateUserForm, UserPasswordChangeForm

# Create your views here.

def index(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    tweet_form = TweetForm(request.POST)
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            if tweet_form.is_valid():
                tweet = tweet_form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                messages.success(request, ('Tweeted successfully!'))
                return redirect('core:index')
        else:
            return render(request, 'index.html', {'tweets':tweets, 'tweet_form': TweetForm})
    else:       
        return redirect('core:login')


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles': profiles})
    else:
        messages.warning(request, ('You must be logged in...'))
        return redirect('core:index')
    
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        tweets = Tweet.objects.filter(user_id=pk).order_by('-created_at')

        if request.method == 'POST':
            #Get current loggedin user
            loggedin_user = Profile.objects.get(user=request.user)

            #Check which action is taken
            action = request.POST['follow']

            if action == "unfollow":
                loggedin_user.follows.remove(profile)
            else:
                loggedin_user.follows.add(profile)
            loggedin_user.save()
        
        
        return render(request, 'profile.html', {'profile':profile, 'tweets':tweets})
    else:
        messages.warning(request, ('You must be logged in...'))
        return redirect('core:index')
    
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('core:login')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:index')
        else:
            messages.warning(request, ('Something went wrong! please try again'))
            return render(request, 'login.html', {})

    
    return render(request, 'login.html', {})


def sign_up(request):
    signup_form = SignupForm()
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, ('Try logging in!'))
            return redirect('core:login')
        else:
            messages.warning(request, ('Something went wrong. Try again!'))
            return render(request, 'sign_up.html', {'signup_form': signup_form})

    
    return render(request, 'sign_up.html', {'signup_form': signup_form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        update_user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if update_user_form.is_valid():
            update_user_form.save()
            messages.success(request, ('Updated successfully!'))
        return render(request, 'update_user.html', {'update_user_form': update_user_form})
    else:
        messages.warning(request, ('You must be logged in...'))
        return redirect('core:login')

def update_password(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        password_form = UserPasswordChangeForm(user=current_user)
        if request.method == 'POST':
            password_form = UserPasswordChangeForm(current_user, request.POST)
            if password_form.is_valid():
                password_form.save()
                messages.success(request, ('Password changed successfully!'))
                messages.success(request, ('Login with new password'))
                return redirect('core:login')
            else:
                #messages.warning(request, ('Something went wrong. Try again!'))
                return render(request, 'password_change.html', {'password_form': password_form})
            
        return render(request, 'password_change.html', {'password_form': password_form})
    else:
        messages.warning(request, ('You must be logged in...'))
        return redirect('core:login')