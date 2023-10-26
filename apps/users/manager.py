from django.contrib.auth.base_user import BaseUserManager 

class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("email is required*")
        
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user 
    

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if not kwargs['is_staff']:
            raise ValueError("Is staff must have superuser")
        
        if not kwargs['is_active']:
            raise ValueError("Is active must have superuser")
        
        if not kwargs['is_superuser']:
            raise ValueError("Is superuser must have superuser")
        
        user = self.create_user(email=email, password=password, **kwargs)
        return user