from django.db import models


class Category(models.Model):
    brand = models.CharField(max_length=100,  )
    type_of_shell = models.CharField(max_length=255)



class Comment(models.Model):
    userName = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName
