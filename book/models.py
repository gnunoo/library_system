from django.db import models
from django.contrib.auth.models import User
# 카테고리
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=200, unique=True,allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/book/category/{self.slug}/'

    class Meta: #테이블 이름 재정의
        verbose_name_plural='Categories'
#post가 도서 테이블
class Post(models.Model):
    title=models.CharField(max_length=20)
    writer=models.CharField(max_length=20,null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(null=True,blank=True)
    author=models.ForeignKey(User,null=True,on_delete=models.CASCADE,blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):#관리자 사이트에서 올라온 데이터를 밑에 형식으로 보여주겠다.
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_absolute_url(self):#절대값 URL 반환:
        return f'/book/{self.pk}/'

# 대여목록
class borrowPost(models.Model):
    title = models.CharField(max_length=20)
    borrow_user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.borrow_user}'