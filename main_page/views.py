from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import post,userinfo,category,post_like_count,post_like
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from my_page.models import homepage
from django.forms.models import model_to_dict
from django.views.decorators.http import require_POST

# Create your views here.

category_list = category.objects.all()

def index(request):
    post_list = post.objects.all().order_by("-id")
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
    curr_post_like_count = post_like_count.objects.get(post=post_to_show)
    post_to_show.view_count+=1
    post_to_show.ranking+=1
    post_to_show.save()
    return render(request,'main_page/post.html',{'POST':post_to_show, 'LIKE_COUNT':curr_post_like_count})

def post_sub(request):
    content = request.POST.get('content')
    summary = request.POST.get('summary')
    title = request.POST.get('title')
    categorys = category.objects.get(id=int(request.POST.get('category')))
    author = userinfo.objects.get(user__username=request.user)
    currpost = post.objects.create(
        title =  title,
        summary = summary,
        category = categorys,
        content =  content,
        view_count = 1,
        comment_count = 0,
        author = author,
        ranking = 1,
    )
    post_like_count.objects.create(
        post=currpost
    )
    homepage.objects.get(owner=author).my_posts.add(currpost.id)
    return HttpResponseRedirect("/")

def post_creat(request):
    if request.user.is_authenticated:
        return render(request,'main_page/post_creat.html')
    else:
        return HttpResponseRedirect("account/login/")

def category_show(request,category_id):
    post_list = post.objects.filter(category__id=category_id).order_by("-id")
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
        post_list = post.objects.all().order_by("-id")
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
    post_list = post.objects.filter(title__icontains=keyword).order_by("-id")
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

def like(request):
    if not request.user.is_authenticated:
        return HttpResponse('请先登录')
    post_id=int(request.GET.get('post'))
    like_post=post_like.objects.filter(post__id=post_id,like_user__user__username=request.user)
    if like_post.exists():
        return HttpResponse('您已点赞')
    else:
        curr_user = userinfo.objects.get(user=request.user)
        curr_post = post.objects.get(id=post_id)
        curr_like_count = post_like_count.objects.get(post=curr_post)
        post_like.objects.create(post=curr_post,like_user=curr_user)
        curr_like_count.count+=1
        curr_like_count.save()
        return HttpResponse(curr_like_count.count)

def favor(request):
    if not request.user.is_authenticated:
        return HttpResponse('请先登录')
    post_id=int(request.GET.get('post'))
    curr_user=homepage.objects.get(owner__user=request.user)
    curr_post = curr_user.favorte.filter(id=post_id)
    if curr_post.exists():
        return HttpResponse("您已收藏")
    curr_user.favorte.add(post_id)
    return HttpResponse("已收藏")

@require_POST
def deletePost(request):
    category_id=request.POST.get('catagory_id')
    curr_category=category_list.get(id=category_id)
    delete_post_id=request.POST.get('post_id')
    if request.user != curr_category.admin.user:
        return HttpResponse("N")
    else:
        delete_post=post.objects.get(id=delete_post_id)
        delete_post.delete()
        return HttpResponse("Y")

def change_data(request):
    new_name = request.POST.get('new_name')
    new_college = request.POST.get('new_college')
    new_department = request.POST.get('new_department')
    new_signature = request.POST.get('new_signature')
    new_photo = request.FILES.get('new_photo')
    curr_user = userinfo.objects.get(user=request.user)
    if new_name:
        curr_user.name = new_name
    if new_college:
        curr_user.college = new_college
    if new_department:
        curr_user.department = new_department
    if new_signature:
        curr_user.signature = new_signature
    if new_photo:
        curr_user.photo = new_photo
    curr_user.save()
    return HttpResponse("成功！")
