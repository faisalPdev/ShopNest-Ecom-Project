from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin



class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, phone_number, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")

        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, phone_number, password=None):
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class Account(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, unique=True,null=True)
    wallet = models.FloatField(null=True,blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin

    # def has_module_perms(self, app_label):
    #     return True

class Address(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=100, null=True)
    housename = models.CharField(max_length=100, null=True)
    town = models.CharField(max_length=100, null=True)
    locality = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.firstname

