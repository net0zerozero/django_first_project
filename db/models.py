from django.db import models
from manage import init_django

init_django()

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Model2(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class ContentRatings(Model):
    title = models.CharField(max_length=255)
    ageLimit = models.IntegerField()
    description = models.TextField()


class Customers(Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=20)
    dateOfBirth = models.DateField()


class Genres(Model):
    title = models.CharField(max_length=255)


class Platforms(Model):
    title = models.CharField(max_length=255)


class Publishers(Model):
    title = models.CharField(max_length=255)


class Products(Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    platform = models.ForeignKey(Platforms, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    releaseDate = models.DateField()
    price = models.IntegerField()
    contentRating = models.ForeignKey(ContentRatings, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    isAvailable = models.BooleanField()


class discount(Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    dateFrom = models.DateField()
    dateUntill = models.DateField()
    price = models.IntegerField()


class Sales(Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    address = models.TextField()
    dateOfSales = models.DateField()


class WishList(Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)


class WL_P(Model2):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    wishList = models.ForeignKey(WishList, on_delete=models.CASCADE)
    
    