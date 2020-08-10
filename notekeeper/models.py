import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from taggit.managers import TaggableManager
from notekeeper_django import settings


class UserManager(BaseUserManager):
    def create_user(self, email, fid):
        if not fid:
            raise ValueError('Firebase Id is required to register a new user')

        if not email:
            raise ValueError('Email is required')

        user = self.model(fid=fid, email=email)
        user.set_unusable_password()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, fid, password):
        user = self.model(email=email, fid=fid, is_superuser=True, is_staff=True)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    fid = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('fid',)


class Note(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    tags = TaggableManager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
