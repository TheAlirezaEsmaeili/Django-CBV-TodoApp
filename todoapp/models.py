from django.db import models

# Create your models here.
class TodoTask(models.Model):

    #user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    #id = models.ForeignKey(on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']