from django.db import models
from django.contrib.auth.models import User


# Carousel
class Carousel(models.Model):
    image = models.ImageField(upload_to='')


# Catalog
class Catalog(models.Model):
    class CarType(models.IntegerChoices):
        UNKNOWN = 0, ('Unknown')
        SEDAN = 1, ('Sedan')
        HATCHBACK = 2, ('Hatchback')
        UNIVERSAL = 3, ('Universal')
        SUV = 4, ('SUV')
        TRUCK = 5, ('Truck')
        MINIVAN = 6, ('Minivan')
        COUPE = 7, ('Coupe')
        ROADSTER = 8, ('Roadster')

    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    carType = models.IntegerField(default=CarType.UNKNOWN, choices=CarType.choices)
    price = models.IntegerField()


# Comment
class CommentCar(models.Model):
    username = models.CharField(max_length=20, null=True)
    comment = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment.name


# Custom User
class CustomUser(User):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    ADMIN = 1
    VipClient = 2
    Client = 3
    USER_TYPE = (
        (ADMIN, 'ADMIN'),
        (VipClient, "VipClient"),
        (Client, 'Client')
    )

    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (MALE, 'MALE'),
        (FEMALE, "FEMALE"),
        (OTHER, 'OTHER')
    )

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип Пользователя', default=Client)
    phone_number = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Гендер')
