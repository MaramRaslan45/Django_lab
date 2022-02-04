from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import login,logout,authenticate
from .forms import userform, updateform
from .models import user, Track


class Register(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        context={}
        username=request.POST['firstname']
        email=request.POST['email']
        password=request.POST['password']
        user.objects.create(first_name=username, last_name=request.POST['lastname'], email=email,password=password,cpassword=request.POST['cpassword'])
        User.objects.create_user(username=username,email=email,password=password)
        context['users'] = user.objects.all()
        # return render(request,'login.html', context)
        return redirect('/login',context)
#
# def register(request):
#     context = {}
#     if (request.method == 'GET') :
#         return render(request,'register.html')
#     else:
#         user.objects.create(first_name=request.POST['firstname']
#                             ,last_name=request.POST['lastname'],email=request.POST['email'],password=request.POST['password'],
#                             cpassword=request.POST['cpassword'])
#         userr= user.objects.all()
#         # return render(request,'login.html', context)
#         return redirect('/login',{'users':userr})


def mylogout(request):
    request.session['username']=None
    logout(request)
    return HttpResponseRedirect ('/login')


def mylogin(request):
    context ={}
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        authuser = authenticate(request,username=username, password=password)
        userf = user.objects.filter(first_name=username, password=password)

        if(authuser is not None and userf is not None):
            login(request, authuser)
            request.session['username']=username
            # request.session['authuser']=authuser
            return HttpResponseRedirect('/home/')
        else:
            context['error'] = 'Invalid Credentials'
            return render(request, 'login.html', context)


def home(request):
    context={}
    context['users']=user.objects.all()
    return render(request,'home.html',context)


class update(View):

    def post(self,request,id):

        users = user.objects.get(id=id)
        users.first_name = request.POST['first_name']
        users.last_name = request.POST['last_name']
        users.email = request.POST['email']
        users.save()
        context = {'users': users}
        return redirect('/home')
    def get(self,request):
        form = updateform()
        return render(request,'update.html', {'form':form})

def insert(request):
    context = {}
    form = userform()
    if (request.method == 'GET'):
        context['form']=form

        return render(request, 'insert.html',context)
    else:
         user.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'],)
         userr = user.objects.all()
         return redirect('/home', {'users': userr})


def delete(request,id):

    users = user.objects.get(id=id)
    users.delete()
    return redirect('/home')


def search(request):
    if (request.method=='GET'):
        name=request.GET.get('names')
        users=user.objects.filter(first_name__iexact=name)
        return render(request,'home.html',{'users':users})
    else:
        return render(request,'home.html', {})



class trackCreateView(CreateView):
    model = Track
    fields = '__all__'



