from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse,reverse_lazy
from users.forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_protect
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required 

from django.contrib.auth.models import User

@csrf_protect
def register(request):
    context = {}
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'shop/product/list.html')
    context['form']=form
    return render(request,'registration/register.html',context)
