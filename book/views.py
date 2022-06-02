
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post,Category,borrowPost
from django.core.exceptions import PermissionDenied
from django.db.models import Q

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context

class PostCreate(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Post
    fields = ['id','title','writer','content','author','category']


    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):

            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/book/')

class PostUpdate(LoginRequiredMixin,UpdateView):
    model=Post
    fields = ['id','title','writer','content','author','category']

    template_name = 'book/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied



def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'book/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )



class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(Q(title__contains=q) ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context


def mypost(requset):
    if requset.method=='POST':
        #대여
        if requset.POST.getlist('book'):
            data=requset.POST.getlist('book')
            data_title=[]
            data_id=[]

            for text in data:
                # id 값과 제목 분리
                data=text.split(',')
                data_title.append(data[1])
                data_id.append(data[0])
            # borrowPost 테이블로 전송
            borrowpost = borrowPost()

            for i in range(len(data_title)):
                borrowpost.title=data_title[i]
                borrowpost.pk=data_id[i]
                borrowpost.borrow_user=requset.user
                borrowpost.save()
                print('insert success')
            #Post 테이블 데이터(cheacke된 데이터) 삭제
            for i in range(len(data_title)):
                post = Post.objects.get(title=data_title[i])
                post.delete()
                print('delete success')
        #반납
        if requset.POST.getlist('borrowbook'):
            data = requset.POST.getlist('borrowbook')
            data_title = []
            data_id = []
            for text in data:
                # id 값과 제목 분리
                data = text.split(',')
                data_title.append(data[1])
                data_id.append(data[0])
            post=Post()
            for i in range(len(data_title)):
                post.title=data_title[i]
                post.pk=data_id[i]

                post.save()
                print('insert success')
            for i in range(len(data_title)):
                borrowpost = borrowPost.objects.get(title=data_title[i])
                borrowpost.delete()
                print('delete success')


    borrowpost=borrowPost.objects.filter(borrow_user=requset.user)
    return render(requset, 'book/borrow_post.html',{'borrowpost':borrowpost})