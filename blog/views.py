from time import time
from django.utils import timezone
from .models import Edited_by, Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse

# Create your views here.

# Post List
class PostList(ListView):
    paginate_by=10
    model=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    

# Post Details

class PostDetail(DetailView):
    model=Post
    context_object_name='post'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        return context
        


class PostNew(CreateView):
    model=Post
    fields=['title','text','author']
    
    def get_success_url(self):
        return reverse("post_detail", kwargs={'pk': self.object.pk})
        
        


class PostEdit(UpdateView):
    model= Post
    fields=['title','text','author']

    def get_success_url(self):
        edit=Edited_by
        edit.post_fk=self.request.user
        edit.edited_date=timezone.now()
        return reverse("post_detail", kwargs={'pk': self.object.pk})


class ModifiedList(ListView):
    model=Edited_by
