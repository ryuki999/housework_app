from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User, Housework, Workreport, Day_rank
from .forms import UsernameForm, PasswordForm, \
                HouseworkNameForm, HouseworkPointForm, HouseworkCheckForm

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


def calendar(request):

    if "login_user" in request.session:
        username = request.session["login_user"]

    nextDate_year = datetime.date.today().year
    nextDate_month = datetime.date.today().month
    nextDate_day = datetime.date.today().day

    day_rank = {}

    if "nextDate_year" in request.GET \
       and "nextDate_month" in request.GET \
       and "nextDate_day" in request.GET:

        nextDate_year = int(request.GET["nextDate_year"])
        nextDate_month = int(request.GET["nextDate_month"])
        nextDate_day = int(request.GET["nextDate_day"])

    argDate = datetime.date(nextDate_year, nextDate_month, nextDate_day)
    calendar_first_day = argDate - datetime.timedelta(
                                      days=(argDate.weekday() + 1))
    calendar_day = calendar_first_day

    for _ in range(0, 35):
        if Day_rank.objects.filter(
          date=calendar_day.strftime("%Y-%m-%d")).exists():
          
            day_info = Day_rank.objects.filter(
              date=calendar_day.strftime("%Y-%m-%d")).order_by('-total_point')
            day_rank_info = {}
            count = 0
            for info in day_info:
                count += 1
                day_rank_info[count] = [info.user_id.username,
                                        info.total_point]
            day_rank[calendar_day.strftime("%Y-%m-%d")] = day_rank_info
        calendar_day += datetime.timedelta(days=1)
    
    calendar_first_day.strftime("%Y-%m-%d")
    params = {
        "login_user": username,
        "rank": day_rank,
        "calendar_first_day": calendar_first_day,
        "nextDate_year": nextDate_year,
        "nextDate_month": nextDate_month,
        "nextDate_day": nextDate_day,
    }
    return render(request, "house/calendar.html", params)


def housework_registration(request):

    # フォームの用意
    housework_name_form = HouseworkNameForm()
    housework_point_form = HouseworkPointForm()
    # 変数の用意
    housework_all = ""
    message = ""
    housework_name = ""
    point = ""
    if "login_user" in request.session:
        username = request.session["login_user"]

    if Housework.objects.exists():
        housework_all = Housework.objects.all().values("housework_name",
                                                       "point")

    # POST送信時の処理
    if request.method == "POST":
        if 'housework_registration' in request.POST:
            housework_name = request.POST["housework_name"]
            point = request.POST["point"]

        # 新規登録処理
            if Housework.objects.filter(housework_name=housework_name).exists():
                message = "既に登録されている家事です"
            else:
                message = "[" + housework_name + "]" + "家事登録完了しました"
                housework = Housework(housework_name=housework_name,
                                      point=point)
                housework.save()

    params = {
        "housework_name_form": housework_name_form,
        "housework_point_form": housework_point_form,
        "login_user": username,
        "housework_all": housework_all,
        "message": message,
    }
    return render(request, "house/housework_registration.html", params)


def housework_report(request):

    housework_name = Housework.objects.all()
    # フォームの用意
    housework_checkform = HouseworkCheckForm(housework_name=housework_name)
    check = ""
    message = ""

    if "login_user" in request.session:
        username = request.session["login_user"]

    # 家事報告処理
    if "housework_report" in request.POST:
        user = User.objects.get(username=username)
        check = request.POST.getlist("housework_check_name")
        message = "家事報告完了しました"

        # get:必ず要素が１つ存在(返り値:インスタンス),filter:要素が複数存在(返り値:Query)
        # filter().first()をつけるとQuerySetの一番初めの要素だけを返してくれる
        for item in check:
            housework = Housework.objects.get(housework_name=item)
            workreport = Workreport(user_id=user,
                                    housework_id=housework,
                                    rep_date=datetime.date.today())
            workreport.save()

            if Day_rank.objects.filter(date=datetime.date.today(),
                                       user_id=user.user_id).exists():
                day_rank = Day_rank.objects.get(date=datetime.date.today(),
                                                user_id=user)
                day_rank.total_point += housework.point
                day_rank.save()
            else:
                total_point = 0
                total_point += housework.point
                day_rank = Day_rank(date=datetime.date.today(),
                                    user_id=user,
                                    total_point=total_point)
                day_rank.save()

    params = {
        "login_user": username,
        "housework_checkform": housework_checkform,
        "check": check,
        "message": message,
    }

    return render(request, "house/housework_report.html", params)
