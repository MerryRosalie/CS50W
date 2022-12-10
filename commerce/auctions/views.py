from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
import datetime
import rfc3339 

from .models import *


def index(request):
    active_listings = AuctionListing.objects.all().filter(active=True)
    return render(request, "auctions/index.html", {
        "active_listings": active_listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":

        if not request.user.is_authenticated:
            return render(request, "auctions/create.html", {
                "message": "Can't create an auction listing without logging in."
            })

        title = request.POST["title"]
        description = request.POST["description"]
        img_url = request.POST["img_url"]
        starting_bid = request.POST["starting_bid"]
        category = request.POST["category"]
        end_time = request.POST["end_time"]
        user = request.user

        f = AuctionListing.objects.create(name = title, image = img_url,
        description = description, start_price = starting_bid,
        category = Category.objects.get(category=category), auctioneer = user, end_time = end_time)

        f.save()

        return HttpResponseRedirect(reverse("index"))

    else:
        min_date = datetime.datetime.now().date() + datetime.timedelta(days=1)
        return render(request, "auctions/create.html", {
            "categories": Category.objects.all(),
            "now" : rfc3339.rfc3339(min_date)[:-9]
        })

def item(request, id):
    item = AuctionListing.objects.all().filter(id = id).first()
    if item:
        try:
            highest_bid = Bid.objects.get(item = item).bid_value
        except Bid.DoesNotExist:
            highest_bid = "-"
        
        return render(request, "auctions/item.html", {
            "item": item,
            "category": item.category.category, 
            "highest_bid": highest_bid
        })
    else:
        return render(request, "auctions/index.html", {
            "message": "Product not found."
        })
