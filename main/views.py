from django.shortcuts import render
from random import randint
from requests import get
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound, JsonResponse
import datetime
import json


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def get_product_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def get_product_json_by_user_id(request, id):
    product_item = Item.objects.filter(user=id)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
@csrf_exempt
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        img = request.POST.get("img")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Item(name=name, price=price, description=description, img=img, amount=amount, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_product(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def increase_amount(request, id):
    item = Item.objects.get(pk=id)
    item.amount = item.amount + 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrease_amount(request, id):
    item = Item.objects.get(pk=id)
    item.amount = item.amount - 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)


@login_required(login_url='/login')
def show_main(request):
    Items = Item.objects.all()
    itemlen = len(Items)
    if(itemlen%3==0):
        row = itemlen - 3
    else:
        row = itemlen - (itemlen %3)

    context = {
        'siswa' : "Muhammad Fachrudin Firdaus",
        'kelas' : 'PBP E',
        'username' : request.user.username,
        'id' : request.user.id,
        'itemlen' : itemlen,
        'items' : Items,
        'last_login': request.COOKIES['last_login'],
        'last_row' : row,
    }
    return render(request, "main.html", context)
    