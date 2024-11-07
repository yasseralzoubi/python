from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email_address=models.CharField(max_length=255)
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def create_user(data):
    User.objects.create(first_name=data["firstname"],last_name=data["lastname"],email_address=data["email"],age=data["age"])




def get_user():
    return User.objects.all()

def deleteuser(id):
    c=User.objects.get(id=id)
    c.delete()




    
