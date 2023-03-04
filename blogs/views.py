from django.http import HttpResponse
from django.shortcuts import render
import random
from .models import *
# Create your views here.

def home(request):
    posts= Posts.objects.order_by('-addedDate')[:8]
    category = Categories.objects.all()
    data ={
        'posts':posts,
        'category':category,
    }
    return render(request,'home.html',data)

def about(request):
    category = Categories.objects.all()
    return render(request,'about.html',{'category':category})

def fullpost(request,id):
    post = Posts.objects.get(postId=id)
    category = Categories.objects.all()
    random_cat = random.sample(list(category),4)
    data ={
        'post':post,
        'category':category,
        'random_cat':random_cat
    }
    return render (request,'fullpost.html',data)

def allcat(request,id):
    category = Categories.objects.all()
    cat = Categories.objects.get(catId=id)
    post = Posts.objects.filter(category=cat)
    data = {
        'cat':cat,
        'post':post,
        'category':category,
    }
    return render (request,'allcat.html',data)