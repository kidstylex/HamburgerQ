from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Quiz,Question,WaitingRoom
from django.contrib.auth import logout
from random import randint

def get_random_id():
        new_name = ""
        for times in range(6):
            new_name += randint(1,9)
        query = WaitingRoom.objects.filter(room_id = new_name)
        if len(query) == 0:
            return new_name
        else:
            get_random_id()


def hi(request):
    return HttpResponse('hi')
    
def play_quiz(request, quiz_name, question_number):
    quiz = get_object_or_404(Quiz, quizz_name = quiz_name)
    q = {'question':quiz.question_set.all()[question_number-1]}
    return render(request,'Game/question_play.html',q)

def home(request):
    return render(request,'Home/mainpage.html')

def log_out(request):
    logout(request)
    return redirect('Game:home')

def how_to_play(request):
    return render(request,'Home/htp.html')

def contact_us(request):
    return render(request,'Home/contact.html')

def login(request):
    return render(request,'Login/login.html')

def login_host(request):
    return render(request,'Login/loginhost.html')

def create_room(request,try_room_name):

    try:
        waiting_room = WaitingRoom(room_name = try_room_name,room_id = get_random_id())
        waiting_room.save()
    except:
        ##create room
        waiting_room = WaitingRoom(room_name = try_room_name,room_id = get_random_id())
        waiting_room.save()
        destiation = '/WRhost/' + waiting_room.room_id + '/'
        return redirect(destiation)
    else:
        ##return error
        return redirect('login/host')
def login_guest(request):
    return render(request,'Login/loginguest.html')

def waiting_room_host(request,room_id):
    context = {'id' : room_id}
    return render(request,'WaitingRoom/WRhost.html',context)

def waiting_room_guest(request,room_id):
    context = {'id' : room_id}
    return render(request,'WaitingRoom/WRguest.html',context)