from django.core.checks import messages
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,TemplateView,UpdateView
from .models import Blog,like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserComment
from django.contrib.auth.models import User
import uuid
# Create your views here.

# def home(request):
#     return render(request,'App_post/home.html',context={})

class Create_blog (LoginRequiredMixin,CreateView):
    model = Blog
    template_name = "App_post/create_blog.html"
    fields = ('blog_title','blog','blog_img')
    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('home'))


from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    user_list = Blog.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'App_post/home.html', { 'blogs': users,'users':users })















# class home(ListView):
#     model = Blog
#     template_name = 'App_post/home.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'blogs'  # Default: object_list
#     paginate_by = 4
#     queryset = Blog.objects.all()  # Default: Model.objects.all()




  
@login_required()
def blog_deitels(request, slug):
    blog = Blog.objects.get(slug=slug)
    Comment_user = UserComment()
    Agary_liked = like.objects.filter(blog=blog, user=request.user)
    if Agary_liked:
        liked = True
    else:
        liked = False

    if request.method == 'POST':
        Comment_user = UserComment(request.POST)
        if Comment_user.is_valid():
            comment = Comment_user.save(commit= False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('App_post:blog_detiels', kwargs={'slug':slug }))
    return render(request,'App_post/blog_detils.html',context={'blog':blog,'comment':Comment_user,'liked':liked,}) 


def BlogDetitel(request,slug):
    blog = Blog.objects.get(slug=slug)
    return render (request,'App_post/blog_detils_1.html',context={'blog':blog,})    

@login_required()
def UserLike(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    Agaeary_liked = like.objects.filter(blog=blog,user=user)
    if not Agaeary_liked:
        like_post = like(blog=blog,user=user)
        like_post.save()
    return HttpResponseRedirect(reverse('App_post:blog_detiels',kwargs={'slug':blog.slug }))
    
@login_required()
def UserUnlike (request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    Ageary_liked = like.objects.filter(blog=blog, user=user)
    Ageary_liked.delete()
    return HttpResponseRedirect(reverse('App_post:blog_detiels',kwargs={'slug':blog.slug}))


class MyBlogs(LoginRequiredMixin,TemplateView):
    template_name = 'App_post/myblog.html'

class EditBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ('blog_title','blog','blog_img')
    template_name = 'App_post/edit.html'

    def get_success_url(self):
        # messages.success(request,'You have successfully Login')
        return reverse_lazy('App_post:MyBlogs',)



def OrderUserProfile(request, username):
    order_user = User.objects.get(username=username)
    return render(request,'App_post/or_profile.html',context={'profile':order_user})





