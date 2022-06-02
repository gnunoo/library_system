from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=200, unique=True,allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/book/category/{self.slug}/'

    class Meta:
        verbose_name_plural='Categories'


class Post(models.Model):
    title=models.CharField(max_length=20)
    writer=models.CharField(max_length=20,null=True,blank=True)
    content=models.TextField(null=True,blank=True)


    created_at=models.DateTimeField(null=True,blank=True)

    author=models.ForeignKey(User,null=True,on_delete=models.CASCADE,blank=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_absolute_url(self):
        return f'/book/{self.pk}/'

class borrowPost(models.Model):
    title = models.CharField(max_length=20)
    borrow_user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.borrow_user}'