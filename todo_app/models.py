from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='children',blank=True,null=True)



class ToDo(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User',related_name='posts',on_delete=models.CASCADE)
    # auth this is an app and we can import User
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    preview = models.ImageField(upload_to='images/', null= True)
    # where we should download our images
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} -----{self.title[:50]}'

    class Meta:
        ordering = ['created_at']