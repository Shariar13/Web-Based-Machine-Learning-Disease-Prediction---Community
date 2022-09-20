from urllib.parse import quote
from django.db.models import fields
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse, request
from django.template import context
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import joblib
from django.contrib.auth import authenticate, login, logout
import joblib
from .models import edit_profile, post
from .models import user_comment
from .forms import edit_profile_form
from .models import chat
from .models import doctor


def home(request):
    return render(request, 'index.html')

def status (request):
    return render (request, 'mini_mental_health_status.html')

def pattern (request):
    return render (request, 'game_pattern.html')

class inbox (ListView):
    model = chat
    template_name = "inbox.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(inbox, self).get_context_data(*args, **kwargs)
        # context['user_message'] = chat.objects.values('name').distinct()
        context['user_message'] = chat.objects.all()
        context['profile_picture'] = edit_profile.objects.all()
        return context



class result (ListView):
    model = doctor
    template_name = "result.html"
    ordering = ['-id']

class find_doctor (ListView):
    model = doctor
    template_name = "find_doctor.html"
    ordering = ['-id']


class profile (ListView):
    model = post
    template_name = "profile.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(profile, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        context['edit_profile'] = edit_profile.objects.all()
        return context


class edit_profile_picture (UpdateView):
    model = edit_profile
    form_class = edit_profile_form
    template_name = "epp.html"
    success_url = ("http://127.0.0.1:8000/profile")


class change_profile_picture (ListView):
    model = edit_profile
    template_name = "c_p_p.html"


def profile_picture_form(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']

        if request.FILES.get('photo', False):
            photo = request.FILES['photo']
            if username == '':
                messages.error(request, "You have to write.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                profile_database = edit_profile(
                    username=username, name=name, photo=photo)
                profile_database.save()
                messages.success(request, "Posted")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            if username == '':
                messages.error(request, "You have to write.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                profile_database = edit_profile(
                    username=username, name=name)
                profile_database.save()
                messages.success(request, "Posted")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def status_form(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        status = request.POST['status']

        if request.FILES.get('photo', False):
            photo = request.FILES['photo']
            if status == '':
                messages.error(request, "You have to write.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                status_database = post(
                    username=username, name=name, status=status, photo=photo)
                status_database.save()
                messages.success(request, "Posted")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            if status == '':
                messages.error(request, "You have to write.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                status_database = post(
                    username=username, name=name, status=status)
                status_database.save()
                messages.success(request, "Posted")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def comment_form(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        post_id = request.POST['post_id']
        comment = request.POST['comment']

        if comment == "":
            messages.error("You have to write something")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            comment_database = user_comment(
                username=username, name=name, post_id=post_id, comment=comment)
            comment_database.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class community (ListView):
    model = post
    template_name = "community.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(community, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        return context


class buddy (ListView):
    model = edit_profile
    template_name = "buddy.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(buddy, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        return context


class buddy_profile (DetailView):
    model = edit_profile
    template_name = "buddy_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(buddy_profile, self).get_context_data(*args, **kwargs)
        context['status'] = post.objects.all()
        context['comment'] = user_comment.objects.all()
        return context

class user_chat (DetailView):
    model = edit_profile
    template_name = "chat.html"

    def get_context_data(self, *args, **kwargs):
        context = super(user_chat, self).get_context_data(*args, **kwargs)
        context['chat_list'] = chat.objects.all()
        return context

def chat_form (request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        chat_user_name = request.POST['chat_user_name']
        chat_name = request.POST['chat_name']
        message = request.POST['message']

        if message == "":
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            chat_database = chat(username = username, name = name, chat_user_name = chat_user_name, chat_name = chat_name, message = message)
            chat_database.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def alzheimer_test(request):
    cls = joblib.load("finalized_model.sav")

    lis = []

    lis.append(float(request.GET['gender']))
    lis.append(float(request.GET['age']))
    lis.append(float(request.GET['ses']))
    lis.append(float(request.GET['el']))
    lis.append(float(request.GET['mms']))
    lis.append(float(request.GET['cd']))
    lis.append(float(request.GET['eti']))
    lis.append(float(request.GET['nwb']))
    lis.append(float(request.GET['asf']))

    ans = cls.predict([lis])
    if ans == 1:
        result = "You Have Alzheimer"
    else:
        result = "You Don't Have Alzheimer"
    return render(request, "result.html", {"result": result})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Username or password incorrect")
            return redirect('/')

    return redirect('/')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                messages.success(request, "Account created successfully.")
                login(request, user)
                return redirect('/')

        else:
            messages.error(request, 'Password not matched')

    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect("/")
