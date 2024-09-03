from django.db import models
from django.utils import timezone
 
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
     
class Book(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()
    epub_file = models.FileField(upload_to='epubs/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books', null=True)

    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.name} - {self.email}'
    
class Certificate(models.Model):
    image = models.ImageField(upload_to='certificates/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
   