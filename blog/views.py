from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import CreatePostForm, CreateCommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Tags, Comments
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# add reverse
# import Paginator
from django.core.paginator import Paginator

# Create your views here.


def post_list(request):
    """
        post list view
        """
    form = CreatePostForm()
    # get all posts posted by the current user
    posts = Post.objects.filter(author=request.user)
    # print(posts)
    return render(request, 'blog/author-posts.html', {'posts': posts, 'form': form})
    # return render(request, 'blog/post_list.html', {'form': form})
    # return render(request, 'blog/post_list.html', {})



class PostListView(ListView):
    """
        post list view
        """
    model = Post
    template_name = 'blog/blogs.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-created_at']


    # def get_context_data:
    #     """ 
    #         check if post is new 
    #     """
    #     context = super().get_context_data()
    #     context['new_posts'] = Post.objects.filter(is_new=True)
    #     return context
    # def get_paginate_by(self, queryset):
    #     """
    #         get the number of posts per page
    #     """

    #     return self.paginate_by
    
    # def get_queryset(self):
    #     """
        
    #     """
    #     queryset = super().get_queryset()
    #     data = queryset[:4]
    #     return data

    # def paginate_queryset(self, queryset, page_size):
    #     """
    #         paginate the queryset
    #     """
    #     paginator = BootstrapPaginator(queryset, page_size)
    #     page_number = self.request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #     return page_obj
class PostDetailView(DetailView):
    """
        post detail view
        """
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_field = 'slug'
    count_hit = True
    extra_context = {
        'comment': Comments.objects.all(),
    }

    form = CreateCommentForm

    def post(self, request, *args, **kwargs):
        """ 
            create comment
        """
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # commit=False to avoid saving to database
            comment.post = get_object_or_404(Post, pk=self.kwargs.get('pk')) # get post from url
            comment.author = request.user # get the current user
            comment.save() # save to database
            return redirect('post-detail', pk=self.kwargs.get('pk')) # redirect to post detail
            # post = self.get_object() #  get the post
            # form.instance.user = request.user #
            # print(form.instance.user,7777)
            # form.instance.post = post
            # form.save()
            # return redirect(reverse('post-detail', kwargs={'pk': post.pk}))
        #     comment = form.save(commit=False) # commit=False to avoid saving the comment to the database
        #     comment.post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        #     comment.author = request.user
        #     comment.save()
        #     return render(request, 'blog/post.html', {'post': comment.post, 'form': form})
        # else:
        #     return render(request, 'blog/post.html', {'post': get_object_or_404(Post, pk=self.kwargs.get('pk')), 'form': form})

    def get_context_data(self, **kwargs):
        """ 
            get tag from a post
        """
        context = super().get_context_data(**kwargs)
        # context['tags'] = Tags.objects.all()
        # get all tags in the post
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        post_comment = Comments.objects.filter(post=self.object.pk)
        # print('new comment', post_comment)
        # find similar posts
        similar_posts = Post.objects.filter(tags__in=post.tags.all()).exclude(pk=post.pk)
        print(similar_posts)
        # if self.request.user.is_authenticated:
        #     self.object.seen_by.add(self.request.user)
        context.update({
            'post_comment': post_comment,
            'post_tags': post.tags.all(),
            'form': self.form,
            'similar_posts': similar_posts,
          
        })
        # print(context)
        # context['form'] = self.form
        # context['post_tags'] = post.tags.all()
        # context['comment'] = Comments.objects.filter(post=post)
        return context


# def post_detail(request, pk):
#     """
#         post detail view
#         """
#     post = get_object_or_404(Post, pk=pk)
#     # print(dir(post), 99)
#     post_tags = post.tags.all() 
#     context = {
#         'post': post,
#         'post_tags': post_tags
#     }
#     return render(request, 'blog/post.html', context)
class AdminUserCheckMixin(UserPassesTestMixin):
    """
        check if the user is an admin
        """
    def test_func(self):
        return self.request.user.is_admin

# admin mixin
class PostCreateView(AdminUserCheckMixin, LoginRequiredMixin, CreateView):
    """
        post create view
        """
    model = Post
    # template_name = 'blog/post_create.html'
    fields = ['title', 'content', 'image', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostUpdateView(AdminUserCheckMixin, LoginRequiredMixin,UserPassesTestMixin , UpdateView):
    """
        post create view
        """
    model = Post
    # template_name = 'blog/post_create.html'
    fields = ['title', 'content', 'image', 'tags']

    def form_valid(self, form):
        """
            set the author of the post to the current user

        Args:
            form: the form object

        Returns:
            the form object
        """        
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
            check if the current user is the author of the post
        """        
        post = self.get_object() # get the post object we trying to update
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(AdminUserCheckMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
        post delete view
        """
    model = Post
    success_url = '/'

    def test_func(self):
        """
            check if the current user is the author of the post
        """        
        post = self.get_object() # get the post object we trying to update
        if self.request.user == post.author:
            return True
        return False
