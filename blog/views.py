
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from blog.modelforms import PostModelForm, PostForm


# Create your views here.
def post_list(request):

    #HttpResponse 사용하기
    #name = 'Django'
    #return HttpResponse('''<h1>Hello {myname} </h1>'''.format(myname=name))

    #Queryset 사용하기
    posts = Post.objects.filter(created_date__lte = timezone.now()).order_by('created_date')

    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):

    if request.method == "POST" :
        form = PostModelForm(request.POST)

        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)

    else :
        form = PostModelForm()
        #print(form)

    return render(request, 'blog/post_edit.html', {'form':form})

def post_new_form(request) :
    if request.method == "POST" :
        form = PostForm(request.POST)

        if form.is_valid() :
            print(form.cleaned_data)
            post = Post(author = request.user, title = form.cleaned_data['title'], text = form.cleaned_data['text'], publish_date = timezone.now())
            post.save()

            return redirect('post_detail', pk=post.pk)


        else :
            print(form.errors)

    else :
        form = PostForm()
        #print(form)

    return render(request, 'blog/post_form.html', {'form':form})