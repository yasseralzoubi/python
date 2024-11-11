from django.db import models

# Create your models here.

class Djos(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Ninjas(models.Model):
    first_name=models.CharField(max_length=255)
    lasr_name=models.CharField(max_length=255)
    dojo=models.ForeignKey(Djos,related_name="ninjas",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)




