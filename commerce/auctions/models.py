from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.fields import BooleanField

class User(AbstractUser):
    def __str__(self):
        return f"User#{self.id} - {self.username}"

class Category(models.Model):
    category = models.CharField(max_length=32)

    def __str__(self):
        return f"Category#{self.id} - {self.category}"

class AuctionListing(models.Model):
    name = models.CharField(max_length=64)
    image = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_price = models.DecimalField(max_digits = 8, decimal_places = 2, validators = [MinValueValidator(0.000001)], blank=True )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null = True, related_name = "categorized")
    auctioneer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user")
    active = models.BooleanField(default=True)
    start_time = models.DateTimeField(auto_now_add = True)
    end_time = models.DateTimeField()
    watchlist = models.ManyToManyField(User, related_name = "watchlist", blank=True, null=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "win", blank=True, null=True)

    def __str__(self):
        return f"Item#{self.id} - {self.name} - {self.category}"

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "bid", blank=True)
    item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name = "bid", blank=True)
    bid_value = models.DecimalField(max_digits = 8, decimal_places = 2)

    def __str__(self):
        return f"Bid#{self.id} - {self.bidder} - {self.item} - {self.bid_value}"

class Comment(models.Model):
    comment = models.TextField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return f"Bid#{self.id} - {self.user} - {self.item}"