from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations=True


    def create_user(self,first_name,last_name,email,password=None,**extra_fields):

        if not email:
            raise ValueError('the givan email must be set')

        email = self.normalize_email(email)
        user=self.model(email=email, first_name=first_name, last_name=last_name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name, last_name,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff true')
        
        return self.create_user(first_name, last_name,email,password,**extra_fields)
