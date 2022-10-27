from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=300)
    price = models.CharField(max_length=20)
    img = models.ImageField(upload_to='static/images/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    funcsi = models.ManyToManyField('Fnksii')

    @property
    def get_url(self):
        return self.slug


    def __str__(self):
        return self.name


class Fnksii(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    userName = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName




