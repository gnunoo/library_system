from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #상속받음
#로그인 페이지
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username') #이름을 가져옴
        password = request.POST.get('password') #비번을 가져옴

        user = authenticate(request, username=username, password=password) #인증

        if user is not None: #인증 되면 로그인 아니면 로그인 페이지로 넘어감
            login(request, user)
            return redirect('book')
    return render(request, 'accounts/login.html')
#회원 가입 페이지
def signup(request):
    form=UserCreationForm() # dajgno에서 제공하는 라이브러리를 불러와서 만듬
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): #db에 저장하고 로그인 페이지로
            form.save()
            return redirect('login')
    context={'form':form}
    #회원가입 페이지를 보여줌
    return render(request, 'accounts/signup.html', context)
#로그아웃
def logoutUser(request):
    logout(request)
    return redirect('login')