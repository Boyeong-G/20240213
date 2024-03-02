from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    dish_name = models.CharField(max_length=30) # 최대 길이 30으로 설정
    ingredient = models.TextField()
    recipe = models.TextField()
    #allergy

    head_image = models.ImageField(upload_to='recipe/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    like_users = models.ManyToManyField(User, related_name='like_recipe')
    
    def __str__(self):
        return f'[{self.pk}]{self.dish_name}'
    
    def get_absolute_url(self):
        return f'/recipe/{self.pk}/'
