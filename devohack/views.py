from django.shortcuts import render
from devohack.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date


# Create your views here.
def index(request):
	posts_list=Post.objects.all().order_by('timestamp')
	page = request.GET.get('page', 1)
	paginator = Paginator(posts_list, 2)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)	
	return render(request, "index.html", {'posts': posts})

def post_view(request, slug):
	context_dict={}
	post = Post.objects.get(slug= slug)
	context_dict['postTitle']= post.postTitle
	context_dict['postContent']= post.content
	context_dict['authorName']= post.author.authorName
	context_dict['date']=post.timestamp.date()
	return render(request, "post.html", context_dict)