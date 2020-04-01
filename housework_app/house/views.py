from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User, Housework, Workreport, Day_rank
from .forms import UsernameForm, PasswordForm

from django.db.models import Q
from django.contrib.auth.decorators import login_required

import datetime


def index(request):
    # フォームの用意
    username_form = UsernameForm()
    password_form = PasswordForm()
    # 変数の用意
    user = ""
    message = ""

    # POST送信時の処理
    if request.method == "POST":

        # ログイン時の処理
        if 'login' in request.POST:
            name = request.POST["username"]
            password = request.POST["password"]
            message = "ログイン画面です"
            if User.objects.filter(username=name, password=password).exists():
                user = User.objects.get(username=name, password=password)
                user = user.username

                params = {
                    "login_user": user
                }
                request.session['login_user'] = user
                return redirect(to="/house/home")
            else:
                user = "ユーザ名或いはパスワードが間違っています"

        # 新規登録処理
        if 'new_registration' in request.POST:
            username = request.POST["username"]
            password = request.POST["password"]
            if User.objects.filter(username=username).exists():
                message = "既に登録されているユーザ名です"
            else:
                message = "新規登録完了しました。ログインしてくだはい"
                user = User(username=username, password=password)
                user.save()

    params = {
        "username_form": username_form,
        "password_form": password_form,
        "message": message,
    }
    return render(request, "house/index.html", params)


def home(request):

    if "login_user" in request.session:
        username = request.session["login_user"]
        user = User.objects.get(username=username)

    today_point_array = []
    today_report_array = []
    yesterday_point_array = []

    if Workreport.objects.filter(user_id=user,
                                 rep_date=datetime.date.today()).exists():

        today_report = Workreport.objects.filter(user_id=user,
                                                 rep_date=datetime.date.today()
                                                 )
        for i in today_report:
            today_report_array.append(i)

    if Day_rank.objects.filter(date=datetime.date.today()).exists():
        today_point = Day_rank.objects.filter(date=datetime.date.today())
        for i in today_point:
            today_point_array.append(i)

    # 昨日の日付を算出
    yesterday_date = datetime.date.today() + datetime.timedelta(days=-1)
    if Day_rank.objects.filter(date=yesterday_date).exists():
        yesterday_point = Day_rank.objects.filter(date=yesterday_date)
        for i in yesterday_point:
            yesterday_point_array.append(i)

    params = {
        "login_user": username,
        "today_report_array": today_report_array,
        "today_point_array": today_point_array,
        "yesterday_point_array": yesterday_point_array,
    }

    return render(request, "house/home.html", params)
