from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import post,userinfo,category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

category_list = category.objects.all()

def index(request):
    post_list = post.objects.all()
    paginator = Paginator(post_list,20)
    curr_page_num = request.GET.get('page')
    try:
        curr_page = paginator.page(curr_page_num)
    except PageNotAnInteger:
        curr_page = paginator.page(1)
    except EmptyPage:
        curr_page = paginator.page(paginator.num_pages)
    var={
        'POST_LIST':post_list,
        'CATEGORY_LIST':category_list,
        'CURR_PAGE':curr_page,
        'PAGINATOR':paginator
    }
    return render(request,'main_page/index.html',var)

def post_show(request,post_id):
    post_to_show = post.objects.get(id=post_id)
    post_to_show.view_count+=1
    post_to_show.ranking+=1
    post_to_show.save()
    return render(request,'main_page/post.html',{'POST':post_to_show})

def post_sub(request):
    content=request.POST.get('content')
    summary = request.POST.get('summary')
    title=request.POST.get('title')
    categorys = category.objects.get(id=int(request.POST.get('category')))
    author = userinfo.objects.get(user__username=request.user)
    post.objects.create(
        title =  title,
        summary = summary,
        category = categorys,
        content =  content,
        view_count = 1,
        comment_count = 0,
        author = author,
        ranking = 1,
    )
    return HttpResponseRedirect("/")

def category_show(request,category_id):
    post_list = post.objects.filter(category__id=category_id)
    paginator = Paginator(post_list,20)
    curr_page_num = request.GET.get('page')
    try:
        curr_page = paginator.page(curr_page_num)
    except PageNotAnInteger:
        curr_page = paginator.page(1)
    except EmptyPage:
        curr_page = paginator.page(paginator.num_pages)
    var={
        'POST_LIST':post_list,
        'CATEGORY_LIST':category_list,
        'CURR_PAGE':curr_page,
        'PAGINATOR':paginator
    }
    return render(request,'main_page/category.html',var)


def search(request):
    keyword = request.GET.get('keyword')
    if not keyword:
        error_msg = '请输入关键字'
        post_list = post.objects.all()
        paginator = Paginator(post_list,20)
        curr_page_num = request.GET.get('page')
        try:
            curr_page = paginator.page(curr_page_num)
        except PageNotAnInteger:
            curr_page = paginator.page(1)
        except EmptyPage:
            curr_page = paginator.page(paginator.num_pages)
        var={
        'POST_LIST':post_list,
        'CATEGORY_LIST':category_list,
        'CURR_PAGE':curr_page,
        'PAGINATOR':paginator,
        'error_msg':error_msg
        }
        return render(request,'main_page/index.html',var)
    post_list = post.objects.filter(title__icontains=keyword)
    paginator = Paginator(post_list,20)
    curr_page_num = request.GET.get('page')
    try:
        curr_page = paginator.page(curr_page_num)
    except PageNotAnInteger:
        curr_page = paginator.page(1)
    except EmptyPage:
        curr_page = paginator.page(paginator.num_pages)
    var={
        'POST_LIST':post_list,
        'CATEGORY_LIST':category_list,
        'CURR_PAGE':curr_page,
        'PAGINATOR':paginator
    }
    return render(request,'main_page/index.html',var)