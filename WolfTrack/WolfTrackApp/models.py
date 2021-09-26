from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
# class Item(models.Model):
#     ToDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)
#     completed = models.BooleanField()
#
#     def __str__(self) -> str:
#         return self.text