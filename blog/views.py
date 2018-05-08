
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


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