from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class Manager(UserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )
        
        user.set_password(password)
        user.is_active = False

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=False, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]

    objects=Manager()

    def __str__(self):
        return self.username or self.email
