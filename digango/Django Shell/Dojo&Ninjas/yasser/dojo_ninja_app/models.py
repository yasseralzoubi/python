from django.db import models

# Create your models here.

class Djos(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    descrbtion=models.TextField(default="old dojo")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Ninjas(models.Model):
    first_name=models.CharField(max_length=255)
    lasr_name=models.CharField(max_length=255)
    dojo=models.ForeignKey(Djos,related_name="ninjas",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



def create_Dojo(data):
    Djos.objects.create(name=data["name"],city=data["city"],state=data["state"])

def get_Djos():
    return Djos.objects.all()

def create_Ninja(data):
    Ninjas.objects.create(first_name=data['firstname'],lasr_name=data['lastname'],dojo=Djos.objects.get(id=data['dojo_id']))
    




