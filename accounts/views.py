from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('book')
    return render(request, 'accounts/login.html')




def signup(request):
    form=UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request, 'accounts/signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')