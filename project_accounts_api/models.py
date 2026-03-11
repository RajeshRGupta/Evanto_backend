from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import uuid
from .manager import UserManager
from django.conf import settings
from datetime import datetime

# Create your models here.

class User(AbstractUser):
    username=None
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=12)
    is_email_varified=models.BooleanField(default=False)
    is_phone_varified=models.BooleanField(default=False)
    # otp=models.CharField(max_length=6,null=True,blank=True)
    email_verification_token=models.CharField(max_length=200,null=True,blank=True)
    forget_password_token=models.CharField(max_length=200,null=True,blank=True)


    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name', 'last_name']

    def name(self):
        return self.first_name + ' ' + self.last_name
    def __str__(self):
        return self.email 

# @receiver(post_save,sender=User)
# def send_email_token(sender,instance,created,**kwargs):
#     try:
#         subject='Your email needs to be verified'
#         message=f'Hi, click on the link to verify email {uuid.uuid4()}'
#         email_from=settings.EMAIL_HOST_USER
#         recipient_list=[instance.email]
#         send_mail(subject,message,email_from,recipient_list)
#     except Exception as e:
#         print(e)
    

class Genre(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    categry=models.CharField(unique=True,max_length=100,null=True,blank=True)



class Eventes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=255,null=True,blank=True)
    details=models.TextField(null=True,blank=True)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    startDate=models.DateField(null=True,blank=True)
    startTime=models.TimeField(null=True,blank=True)
    adderss=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    eventMode=models.CharField(max_length=100,null=True,blank=True)
    language=models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField()
    evquntity = models.IntegerField(default = 0)
    evsoldquntity = models.IntegerField(default = 0)
    deactivate=models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     current_datetime = datetime.now()
    #     event_datetime = datetime.combine(self.startDate, self.startTime)
    #     if event_datetime > current_datetime:
    #         self.deactivate = False  
    #     else:
    #         self.deactivate = True  
    #     super().save(*args, **kwargs)

# @receiver(post_save, sender=Eventes)
# def update_deactivate_field(sender, instance, created, *args, **kwargs):
#     current_datetime = datetime.now()
#     event_datetime = datetime.combine(instance.startDate, instance.startTime)
#     print('////////////////////////////////////////')
#     print(current_datetime)
#     print(event_datetime)
#     if event_datetime > current_datetime:
#         instance.deactivate = False  

#     else:
#         instance.deactivate = True
#     instance.save(update_fields=['deactivate'])



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    events = models.ForeignKey(Eventes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)


