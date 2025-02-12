from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import  login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from .models import Profile
# Create your views here.

def register(request):
    
    if request.method== 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            print('my User Name:',username)
            messages.success(request,f'Account created for {username}')
            form.save()
            return redirect('login')
    else:
        form=UserRegisterForm()

    return render(request,'users/register.html',{"form":form,'blog_categories':get_blog_categories()})


def logout_view(request):  
    
    context={'blog_categories':get_blog_categories()}
    if request.method == 'POST':
        logout(request)
        messages.success(request,f'You have been logged out!')
        return redirect("login") 
    
    else:
        return render(request,'users/logout.html',context)

@login_required
def profile(request):
        
        if request.method=="POST":
            u_form= UserUpdateForm(request.POST, instance= request.user)
            p_form=ProfileUpdateForm(request.POST, request.FILES ,instance= request.user.profile)

            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()

                messages.success(request,f'Your profile has been updated successfully!')
                return redirect("profile") 


        else:
            u_form= UserUpdateForm( instance= request.user)
            p_form=ProfileUpdateForm(instance= request.user.profile)



        context={'u_form':u_form,
                 'p_form':p_form,
                 'blog_categories':get_blog_categories()}



        return render(request,'users/profile.html',context)

def get_blog_categories():

    return ""

  