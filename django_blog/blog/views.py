from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostCreation
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
context = {'post': Post.objects.all(), 'page_title': 'blog'}
def home(request):
    return render(request,'blog/home.html', context)
def about(request):
    return render(request,'blog/about.html', {'data':'render_test'})

@login_required
def post_update(request,pk):
    post_object = Post.objects.get(id=pk)
    if request.method == "POST":
        post = PostCreation(request.POST, instance= post_object)
        if post.is_valid():
            post.save()
    else:
        post = PostCreation(instance = post_object)

   
    return render(request,'blog/post.html',{'post':post})

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    paginate_by = 5
    ordering = ['-date_posted']

class UserPostList(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user_post.html'
    paginate_by = 5
    

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author= user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title","content"]

    # success_url = reverse_lazy('blog-home')
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ["title","content"]

    def test_func(self):
        post = self.get_object()

        if post.author == self.request.user: 
            return True
        
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = reverse_lazy("blog-home")
    def test_func(self):
        post = self.get_object()

        if post.author == self.request.user: 
            return True
        
        return False



    
         



    
