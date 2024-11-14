from django.db import models

# Create your models here.

class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


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
    
    





    
