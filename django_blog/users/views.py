from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import MyCustomForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    context = {}
    if request.method == 'POST':
        form = MyCustomForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            form.save()
            messages.success(request, f'Account Created Successfully for {first_name}. You can login here')
            return redirect('login')
        context['form'] = MyCustomForm()
        
        
    else:
        form = MyCustomForm()
        context = {'form':form}
    return render(request,'users/register.html',context)


class MyLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            messages.success(request, "You are logged out successfully.")
        return super().dispatch(request, *args, **kwargs)
@login_required    
def profile(request):
    return render(request, 'users/profile.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username = username, password = password )
#         if user is not None:
#             login(request,user)
#             print(user)
#             print(user.is_authenticated)
#             print(request.user)
#             return redirect('/admin')
#         else:
#             print(request.user)
#             context = {'error':'Invalid Username or Password'}
#             return render(request,'users/login.html',context)


        
    
#     return render(request,'users/login.html',{})



# def logout_view(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect('login')
#     return render(request,'users/logout.html',{})



             
        

    