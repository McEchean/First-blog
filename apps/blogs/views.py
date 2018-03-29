from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json
from django.db.models import Q
from .models import BlogModel, CategoryModel, BoxModel
from users.models import UserProfile,UserCommentModel, ContactModel
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.models import TagPropertyModel
from .forms import MessageForm


# Create your views here.

class HomepageView(View):
    def get(self, request):
        return render(request, 'homepage.html')


class BlogHomepageView(View):
    def get(self, request):
        user = UserProfile.objects.get(username='root')
        all_blogs = BlogModel.objects.all()
        all_category = CategoryModel.objects.all()
        #搜索
        search = request.GET.get('search','')
        if search:
            all_blogs = BlogModel.objects.filter(Q(title__icontains=search)|Q(content__icontains=search)|Q(desc__icontains=search))

        #分类
        cat = request.GET.get('category','')
        if cat:
            all_blogs = BlogModel.objects.filter(category_id=int(cat))

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blogs, 3, request=request)
        blogs = p.page(page)

        return render(request, 'Blog-homepage.html', {
            'all_blogs': blogs,
            'all_categorys': all_category,
            'user_root': user
        })


class BlogDetailView(View):
    def get(self,request,blog_id):
        user = UserProfile.objects.get(username='root')
        all_category = CategoryModel.objects.all()
        blog = BlogModel.objects.get(id= int(blog_id))
        tags = TagPropertyModel.objects.filter(blog_id=blog_id)


        all_comments = UserCommentModel.objects.filter(blog=blog_id)
        all_comments = all_comments.order_by('-add_time')
        tag_in = request.GET.get('tag', '')
        cat = request.GET.get('category', '')
        search = request.GET.get('search', '')
        if cat or tag_in or search:
            all_blogs =[]
            if cat:
                all_blogs = BlogModel.objects.filter(category_id=int(cat))
            if tag_in:
                all_tag_property = TagPropertyModel.objects.filter(tag_id=int(tag_in))
                for i in all_tag_property:
                    all_blogs.append(i.blog)
            if search:
                all_blogs = BlogModel.objects.filter(Q(title__icontains=search) |\
                                                     Q(content__icontains=search) | \
                                                     Q(desc__icontains=search))

            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_blogs, 3, request=request)
            blogs = p.page(page)

            return render(request, 'Blog-homepage.html', {
                'all_blogs': blogs,
                'all_categorys': all_category,
                'user_root': user
            })
        return render(request,'Blog-detail-page.html',{
            'blog':blog,
            'all_categorys': all_category,
            'user_root': user,
            'tags': tags,
            'all_comments':all_comments
        })


class AddCommentView(View):
    def post(self,request,blog_id):
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            # blogid = request.POST.get('blog_id','')
            username = request.POST.get('username','')
            email = request.POST.get('email','')
            message = request.POST.get('content','')
            comment = UserCommentModel()
            user_new = UserProfile.objects.get(email=email)
            if not user_new:
                user_new = UserProfile()
                user_new.nick_name = username
                user_new.email = email
                user_new.save()
            comment.user = user_new
            comment.blog_id = int(blog_id)
            comment.comment = message
            comment.save()
            return HttpResponse(json.dumps({'status':'success'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status':'fail','msg':'提交的信息有点错误，请再确认一下'}), content_type='application/json')


class BoxView(View):
    def get(self,request):
        all_box = BoxModel.objects.all().order_by('-add_time')
        return render(request, 'Box.html', {
            'all_boxes':all_box
        })


class ContactView(View):
    def get(self,request):
        return render(request,'Contact.html')


class SuggestView(View):
    def post(self,request):
        suggest_form = MessageForm(request.POST)
        if suggest_form.is_valid():
            user = request.POST.get('username','')
            email = request.POST.get('email','')
            suggest = request.POST.get('content','')
            user_new = UserProfile.objects.get(email=email)
            if not user_new:
                user_new = UserProfile()
                user_new.nick_name = user
                user_new.email = email
                user_new.save()
            suggest_obj = ContactModel()
            suggest_obj.user = user_new
            suggest_obj.suggest = suggest
            suggest_obj.save()
            return HttpResponse(json.dumps({'status': 'success', 'msg':'提交成功'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status': 'fail', 'msg':'提交的信息有点错误，请再确认一下'}), content_type='application/json')



