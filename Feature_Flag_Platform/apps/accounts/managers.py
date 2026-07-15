from django.contrib.auth.base_user import BaseUserManager

'''
    This class manages all user creation and super user creation using django 
    Base user manager and its methods for email and password
'''

class UserManager(BaseUserManager):
    # Creating normal user
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user
    # creating superuser
    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)

        extra_fields.setdefault("is_superuser", True)

        return self.create_user(
            email,
            password,
            **extra_fields
        )