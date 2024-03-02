from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    summary = models.CharField(max_length=30) # 최대 길이 30으로 설정
    question = models.TextField()
    
    head_image = models.ImageField(upload_to='question/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}]{self.summary}'
    
    def get_absolute_url(self):
        return f'/question/{self.pk}/'
    

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'[{self.author}]{self.comment}'
    
    def get_absolute_url(self):
        return f'{self.question.get_absolute_url()}#comment-{self.pk}'