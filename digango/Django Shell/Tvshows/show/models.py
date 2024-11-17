from django.db import models
import re
import bcrypt
from django.utils import timezone

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        # التحقق من طول الاسم الأول
        if len(postData['title']) < 2:
            errors["title"] = "title should be at least 2 characters"
        
        # التحقق من طول الاسم الأخير
        if len(postData['network']) < 4:
            errors["network"] = "network should be at least 4 characters"

        # التحقق من طول كلمة المرور
        if len(postData['des']) < 10:
            errors["des"] = "des should be at least 10 characters"
        # التحقق من التاريخ في الماضي 
        if postData.get('release_date'):
            release_date = postData['release_date']
            release_date = timezone.datetime.strptime(release_date,'%b %d, %Y').date()
            if release_date > timezone.now().date():
                errors["release_date"] = "release date should be in the past"

                
        return errors


# Create your models here.

class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = ShowManager()


def create_show(data):
    Show.objects.create(title=data['title'], network=data['network'],release_date=data['release'],description=data['des'] )

def get_all_show():
    return Show.objects.all()

def delete_show(id):
    c=Show.objects.get(id=id)
    c.delete()

def get_by_id(id):
    return Show.objects.get(id=id)

def update_show(data):
    id =int(data['id'])
    D=Show.objects.get(id=id)
    D.title=data['title']
    D.network=data['network']
    D.release_date=data['release']
    D.description=data['des']
    D.save()
    
    





    
