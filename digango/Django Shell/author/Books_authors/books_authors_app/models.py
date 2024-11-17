from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=255)
    desc_Text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    notes = models.TextField()


def add_Book(Data):
    Book.objects.create(title=Data["title_book"] , desc_Text=Data["desc_book"])

def get_books():
    return Book.objects.all()

def get_book_id(book_id):
    return Book.objects.get(id=book_id)


#related to authors
def add_author(Data):
    Author.objects.create(first_name=Data["firstname"],last_name=Data["last_name"],notes=Data["note"] )



def get_authors():
    return Author.objects.all()

def get_author_id(id):
    return Author.objects.get(id=id)

def add_book_to_auther():
    this_book = Book.objects.get(id=id)     #
    this_author = Author.objects.get(id=id)

    this_author.books.add(this_book)

