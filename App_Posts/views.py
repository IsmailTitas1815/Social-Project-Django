from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from App_Posts.models import Likes, Post
from App_Login.models import Follow


@login_required
def home(request):
    following_list = Follow.objects.filter(follower= request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following')) #ami jadr follow kori tadr nam jodi post e thake, mane tara jodi kono post er author hoy tahole shegulo ashbe.
    print(posts)
    liked_post = Likes.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list("post", flat=True)

    if request.method == "GET":
        search = request.GET.get('search',"")
        result = User.objects.filter(username__icontains = search)

    return render(request, "App_Posts/home.html",context={'title':'Home', "search": search, "result":result, "posts":posts, "liked_post_list":liked_post_list})


@login_required
def liked(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Likes.objects.filter(post= post, user = request.user)
    if not already_liked:
        liked_post = Likes(post= post, user = request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('home'))

@login_required
def unliked(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Likes.objects.filter(post = post, user = request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))
