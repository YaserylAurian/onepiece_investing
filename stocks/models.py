from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Please provide a valid username")
        user = self.model(username = username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_user(self, username = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)
    
    def create_superuser(self, username = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, blank=True, default='', unique=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.username