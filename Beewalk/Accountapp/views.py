from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Member
from .forms import SignUpForm, LoginForm


def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('accountapp:login')  # 회원가입 후 로그인 페이지로 리디렉션
    else:
        form = SignUpForm()

    return render(request, 'Accountapp/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                print("success")
                login(request, user)
                return redirect('countapp:index')
            else:
                form.add_error(None, '잘못된 이메일 또는 비밀번호를 입력했습니다.')
    return render(request, 'Accountapp/login.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Member, Follow

@login_required
def follow(request, user_id):
    user_to_follow = get_object_or_404(Member, id=user_id)
    if request.user != user_to_follow:
        follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        if created:
            return redirect('profile', user_id=user_id)
        else:
            return HttpResponseForbidden("Already following this user.")
    else:
        return HttpResponseForbidden("You cannot follow yourself.")

@login_required
def unfollow(request, user_id):
    user_to_unfollow = get_object_or_404(Member, id=user_id)
    if request.user != user_to_unfollow:
        Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
        return redirect('profile', user_id=user_id)
    else:
        return HttpResponseForbidden("You cannot unfollow yourself.")

# def login_view(request):
#     is_user = request.session.get('is_user', False)
#     print(is_user)
#     form = LoginForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             passwords = form.cleaned_data['password']
#             try:
#                 user = Member.objects.get(email=email)
#             except Member.DoesNotExist:
#                 form.add_error(None, '존재하지 않는 회원입니다.')
#             else:
#                 if check_password(passwords, user.password):
#                     login(request, user=user)
#                     request.session['is_user'] = True  # 로그인 성공 시 세션에 is_ok 값을 저장
#                     return redirect('countapp:index')
#                 else:
#                     form.add_error(None, '잘못된 이메일 또는 비밀번호를 입력했습니다.')
#         else:
#             form = LoginForm()
#
#     return render(request, 'Accountapp/login.html', {'form': form, 'is_user':is_user})

def logout_view(request):
    logout(request)
    return redirect('/account/login')