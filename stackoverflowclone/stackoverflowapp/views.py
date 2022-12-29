from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView,ListView,DetailView
from stackoverflowapp.forms import RegistrationForm,LoginForm,QuestionForm,AnswerForm
from stackoverflowapp.models import Answer, MyUser, Question
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.urls import reverse_lazy
# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must Login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

desc=[signin_required,never_cache]
@method_decorator(desc,name="dispatch")
class IndexView(CreateView,ListView):
   template_name="home.html"
   form_class=QuestionForm
   model=Question
   success_url=reverse_lazy("index")
   context_object_name="questions"
   
   def form_valid(self, form):
      form.instance.user=self.request.user
      return super().form_valid(form)
   
   def get_queryset(self):
       return Question.objects.all().exclude(user=self.request.user)
   
   
class SignUpView(CreateView):
       model=MyUser
       form_class=RegistrationForm
       template_name="register.html"
       success_url=reverse_lazy("signup")

class LoginView(FormView):
       form_class=LoginForm
       template_name="login.html"
       
                                                               # def get(self,request,*args,**kwargs):
                                                               #    form=LoginForm()
                                                               #    return render(request,"login.html",{"form":form})
   
      
       def post(self,request,*args,**kwargs):
          form=LoginForm(request.POST)
          if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
               login(request,usr)
               return redirect("index")
            else:
               return render(request,"login.html",{"form":form})

@method_decorator(desc,name="dispatch")           
class QuestionDetailView(DetailView):
   model=Question
   template_name="question_deatil.html"
   pk_url_kwarg: str="id"
   context_object_name: str="question"
   form_class=AnswerForm
   
#localhost:8000/question/{id}/answer

def add_answer(request,*args,**kwargs):   
   if request.method=="POST":
         form=AnswerForm(request.POST)
         if form.is_valid():
             answer=form.cleaned_data.get("answer")
             qid=kwargs.get("id")
             question=Question.objects.get(id=qid)
             Answer.objects.create(user=request.user,answer=answer,question=question)
             return redirect("index")
         else:
             return redirect("index")

def upvote_view(request,*args,**kwargs):
   ans_id=kwargs.get("id")
   ans=Answer.objects.get(id=ans_id)
   ans.upvote.add(request.user)
   ans.save()
   return redirect("index")

def remove_answer(request,*args,**kwargs):
   ans_id=kwargs.get("id")
   Answer.objects.get(id=ans_id).delete()
   return redirect("index")

desc      
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
 
       
       
