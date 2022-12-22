from django.db import models
from ckeditor.fields import RichTextField

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
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=20)
    img = models.ImageField(upload_to='static/images/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    funcsi = models.ManyToManyField('Fnksii')
    
    @property
    def get_url(self):
        return self.slug


    def __str__(self):
        return self.name


class Technique(models.Model):
    name = models.CharField(max_length=200, verbose_name="Производитель", null=True, blank=True)
    type_corpuse = models.CharField(max_length=200, verbose_name="Тип корпуса", null=True, blank=True)
    power_level = models.CharField(max_length=200, verbose_name="Уровень мощности", null=True, blank=True)
    type_signal = models.CharField(max_length=200, verbose_name="Тип обработки сигнала", null=True, blank=True)
    count_channel = models.CharField(max_length=200, verbose_name="Количество каналов", null=True, blank=True)
    max_usilenie = models.CharField(max_length=200, verbose_name="Максимальное акустическое усиление*, (дБ)", null=True, blank=True)
    max_vuzd = models.CharField(max_length=200, verbose_name="Максимальное акустическое усиление*, (дБ)", null=True, blank=True)
    battery = models.CharField(max_length=200, verbose_name="Батарейка", null=True, blank=True)
    count_programm = models.CharField(max_length=200, verbose_name="Количество программ прослушивания", null=True, blank=True)


    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Fnksii(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Comment(models.Model):
    userName = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName



class Banner(models.Model):
    image = models.ImageField(upload_to='static/images/banner', blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title