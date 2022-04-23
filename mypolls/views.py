from turtle import title
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse, HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from uuid import uuid4
from datetime import datetime, timezone
import pytz
import json
import ast

from .models import Polls, User, Choices

check_time = 259200.0


def checkToken(data):
    tz = pytz.timezone("Asia/Calcutta")
    now = datetime.now(tz)
    diff = now - data
    return diff.total_seconds() < check_time


def jsonToString(string):
    return json.dumps(string, separators=(',', ':'))


def index(request):
    return JsonResponse({"status": "ok"})


@csrf_exempt
def mytry(request):
    data = request.POST.get('data')
    data = ast.literal_eval(data)
    return JsonResponse({"status": "ok", "data": data})


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        auth = authenticate(request, username=username, password=password)
        if auth:
            uid = uuid4()
            user = User.objects.get(username=auth.username)
            user.token = uid
            # user.token_date = datetime.now()
            status = checkToken(user.token_date)
            if not status:
                user.token_date = datetime.now()
            user.save()
            login(request, user)
            name = {'a': 1, 'b': 2}
            return JsonResponse({"message": "Logged In", "token-status": status, "status": 200, "token": user.token})
        else:
            return JsonResponse({"status": 401, "message": "Invalid Crendentials"})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


@ csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logged Out", "status": 200})


@ csrf_exempt
def register(request):
    if request.method == "POST":
        uname = request.POST["username"]
        username = uname.lower()
        email = request.POST["email"]
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]

        # Ensure password matches confirmation
        password = request.POST["password"]

        check1 = User.objects.filter(email=email)
        check2 = User.objects.filter(username=uname)
        if check1:
            return JsonResponse({
                "message": "Email Id Exists. Please Login!",
                "status": 409
            })
        elif check2:
            return JsonResponse({
                "message": "Username Exists. Please Login!",
                "status": 409
            })
        # Attempt to create new user
        else:
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
            except IntegrityError:
                return JsonResponse({
                    "message": "Username already taken.",
                    "status": 409
                })
            login(request, user)
            return JsonResponse({"status": 200, "message": "User Created Successfully"})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


@csrf_exempt
def create_poll(request):
    if request.method == "POST":
        auth = request.headers.get('Authorization')
        user = User.objects.get(token=auth)
        if str(auth) == str(user.token) and checkToken(user.token_date):
            title = request.POST["title"]
            description = request.POST["description"]
            poll = Polls.objects.create(
                title=title, description=description, user=user)
            choice = request.POST["choices"]
            choice = ast.literal_eval(choice)
            for i in choice:
                temp = Choices.objects.create(poll=poll, title=i)
                poll.choices.add(temp)
                temp.save()
            poll.save()
            return JsonResponse({"status": 200, "message": "Poll Created Successfully"})
        else:
            return JsonResponse({"status": 401, "message": "Unauthorized"})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


@csrf_exempt
def choose(request):
    auth = request.headers.get('Authorization')
    user = User.objects.get(token=auth)
    data = json.loads(request.body)
    print(data['postId'])
    choice_id = data['postId']
    choice = Choices.objects.get(id=choice_id)
    if request.method == "GET":
        return JsonResponse(choice.serialize())
    elif request.method == "PUT":
        if user not in choice.users.all():
            choice.users.add(user)
            choice.votes += 1
            choice.save()
        return JsonResponse(choice.serialize())
    else:
        return JsonResponse({"error": "Error Encountered"}, status=400)
