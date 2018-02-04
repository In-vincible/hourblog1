from django.shortcuts import render
from devohack.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date


# Create your views here.
def index(request):
	categoryList = Category.objects.all()
	posts_list=Post.objects.all().order_by('timestamp')
	popular_posts = Post.objects.all().order_by('viewCount')[:4]
	popularPostsArray = []
	for p in popular_posts:
		pop = {}
		pop['title'] = p.postTitle
		pop['shortDescription'] = p.content[:180]+"..."
		#print(pop['shortDescription'])
		pop['slug'] = p.slug
		popularPostsArray.append(pop)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts_list, 2)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)	
	#print(categoryList)
	return render(request, "index.html", {'posts': posts, 'categories':categoryList, 'popular_posts':popularPostsArray})

def post_view(request, slug):
	categoryList = Category.objects.all()
	context_dict={}
	context_dict['categories']=categoryList
	post = Post.objects.get(slug= slug)
	post.viewCount += 1
	post.save()
	#print(post.viewCount) 
	tags = post.tag.all()
	#print(tags)
	context_dict['tags']= tags
	context_dict['postTitle']= post.postTitle
	context_dict['postContent']= post.content
	context_dict['authorName']= post.author.authorName
	context_dict['date']=post.timestamp.date()
	return render(request, "post.html", context_dict)

def category_view(request, slug):
	categoryList = Category.objects.all()
	category = Category.objects.get(slug = slug)
	posts_list = Post.objects.filter(category__categoryId = category.categoryId)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts_list, 2)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, "category.html", {'posts':posts, 'category':category, 'categories':categoryList})

def tag_view(request, slug):
	categoryList = Category.objects.all()
	tag = Tag.objects.get(slug = slug)
	posts_list = Post.objects.filter(tag__tagId = tag.tagId)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts_list, 2)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, "tag.html", {'posts':posts, 'tag':tag, 'categories':categoryList})

def aboutus_view(request):
	categoryList = Category.objects.all()
	return render(request, "aboutus.html", {'categories':categoryList}) 