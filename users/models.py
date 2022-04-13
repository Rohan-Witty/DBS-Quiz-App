from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(
        self, id, password=None, is_staff=False, active=True, is_admin=False
    ):
        """
        Creates and saves a User with the given email and password.
        """
        if not id:
            raise ValueError("Users must have an ID")

        user = self.model(
            id=id,
        )

        user.set_password(password)
        user.save(using=self._db)
        user.active = active
        user.admin = is_admin
        return user

    def create_superuser(self, id, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            id,
            password=password,
        )
        user.admin = True
        user.active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=13, primary_key=True)
    USERNAME_FIELD = "id"
    name = models.CharField(max_length=100)
    NAME_FIELD = "name"
    password = models.CharField(max_length=128)
    PASSWORD_FIELD = "password"
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)  # superuser
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.id

    def get_full_name(self):
        return self.id

    def get_short_name(self):
        return self.id

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def is_superuser(self):
        return self.admin

    class Meta:
        db_table = "student"
