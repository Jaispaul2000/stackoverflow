from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models import Count

# class UserProfile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)

class MyUser(AbstractUser):
    phone=models.CharField(max_length=20)
    profile_pic=models.ImageField(upload_to="profilepics",null=True)


class Question(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    description=models.CharField(max_length=120)
    image=models.ImageField(upload_to="stackimage",null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    
    @property
    def fetch_answer(self):
        answer=self.answer_set.all().annotate(u_count=Count('upvote')).order_by('-u_count')
        return answer
    
    def __str__(self):
        return self.description

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    answer=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    upvote=models.ManyToManyField(MyUser,related_name="upvote")