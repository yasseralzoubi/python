from django.db import models
import re
import bcrypt

class RegistrationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}


        # التحقق من طول الاسم الأول
        if len(postData['first_name']) < 3:
            errors["first name"] = "First name should be at least 3 characters"
        
        # التحقق من طول الاسم الأخير
        if len(postData['last_name']) < 4:
            errors["last name"] = "Last name should be at least 4 characters"

                # التحقق من صحة البريد الإلكتروني باستخدام Regex
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address!"

        # التحقق من عدم وجود البريد الإلكتروني مسبقاً في قاعدة البيانات
        if Registration.objects.filter(email=postData['email']).exists():
            errors["email"] = "Email is already in use"

        
        # التحقق من طول البريد الإلكتروني (يمكن إضافة المزيد من التحقق)
        if len(postData['email']) < 5:
            errors["email"] = "Email should be at least 5 characters"
        
        # التحقق من طول كلمة المرور
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        
        # التحقق من تطابق كلمة المرور مع التأكيد
        if postData['password'] != postData['confirm_pw']:
            errors["confirm_pw"] = "Passwords do not match"
        
        return errors
    


# Create your models here.
class Registration (models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=60)
    confirmPw = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegistrationManager()




def insert_new_user_DB(Data):
    hashed_password = bcrypt.hashpw(Data['password'].encode(), bcrypt.gensalt()).decode()
    user = Registration.objects.create(firstname=Data['first_name'],  lastname=Data['last_name'] , email=Data['email'] , password=hashed_password)
    return user



def get_all_user():
    all_user=Registration.objects.all()
    return all_user




def authenticate_user(email, password):
        user = Registration.objects.filter(email=email)
        user_passowrd=user[0].password

        return bcrypt.checkpw(password.encode(), user_passowrd.encode())
            


    
