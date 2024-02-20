from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User,AbstractUser, AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

STATUS=(
    ('ACTIVE','active'),
    ('INACTIVE','inactive')
)

class Category(models.Model):
    name = models.CharField(max_length=200, null=True,blank=False)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Vendor(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length = 250)
    lastname = models.CharField(max_length = 250, blank=False, null=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length = 250, blank=False)
    revenue = models.CharField(max_length = 250, blank=False)
    category = models.ManyToManyField(Category,related_name='vendor_category', blank=True)
    no_of_employees = models.IntegerField(null=True, blank=False)
    pancard_no = models.CharField(max_length = 250, null=True, blank=False)
    gst_no = models.CharField(max_length = 250, null=True, blank=False)
    mobile = models.CharField(max_length = 250, null=True, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_requestadmin = models.BooleanField(default=False)
    active_status = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class RequestAdmin(AbstractUser):
#     firstname = models.CharField(max_length = 250)
#     lastname = models.CharField(max_length = 250, blank=False, null=True)
#     email = models.EmailField(blank=False, unique=True)
#     password = models.CharField(max_length = 250, blank=False)

#     USERNAME_FIELD = "email"

#     def __str__(self):
#         return self.firstname
    

    


class RequestForProposal(models.Model):
    item_name = models.CharField(max_length=250, blank=False)
    rfp_no = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(default=0, null=False, blank=False)
    last_date = models.DateField()
    minimum_price = models.FloatField(max_length=250, null=False, blank=False)
    maximum_price = models.FloatField(max_length=250, null=False, blank=False)
    categories = models.ManyToManyField(Category, related_name='category', blank=False)
    vendor = models.ManyToManyField(Vendor,related_name='vendor', blank=False)
    item_description = models.TextField(null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name
    
class Quotes(models.Model):
    rfp = models.ForeignKey(RequestForProposal, on_delete = models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_price = models.CharField(max_length=250, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    total_cost = models.CharField(max_length=250, blank=True, null=True)
    item_description = models.TextField(blank=True)
