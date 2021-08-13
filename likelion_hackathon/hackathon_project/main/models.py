from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Book(models.Model):# 소설,시,비문학,에세이에 공통적으로 사용되는 모델입니다.
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    read_date = models.DateField()
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()
    question5 = models.TextField()
    genre = models.CharField(max_length=10)
    author=models.ForeignKey(User, related_name='books',on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Free(models.Model): #자유 양식 작성을 위한 모델입니다.
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    read_date = models.DateField()
    question1 = models.TextField()
    author=models.ForeignKey(User,related_name='frees',on_delete=CASCADE)

    def __str__(self):
        return self.title