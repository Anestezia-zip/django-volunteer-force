from django.views.generic.detail import DetailView
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View, generic
from .models import Post, Region, UserProfile
from .forms import PostForm, UserProfileForm
from django.utils.text import slugify
from django.contrib import messages
from unidecode import unidecode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


class AllPostsView(generic.ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 6
    context_object_name = 'posts_list'

    def get(self, request):
        posts = Post.objects.all().order_by('-date_created')
        paginator = Paginator(posts, self.paginate_by)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        # Updated context to pass the posts_list variable
        context = {'posts_list': posts}
        return render(request, self.template_name, context)


class PostDetail(DetailView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                'post': post
            }
        )


class UserPostsView(View):
    template_name = 'profile.html'

    def get(self, request):
        user = request.user
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        user_posts = Post.objects.filter(author=user)

        return render(
            request,
            self.template_name,
            {'user_profile': user_profile, 'user_posts': user_posts}
        )


@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    form = UserProfileForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def add_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            # Generate a unique slug based on the title
            base_slug = slugify(unidecode(post.title))
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            post.slug = slug
            post.save()
            return redirect('profile')

    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('profile')
    form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'edit_post.html', context)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect('profile')


def donate(request):
    return render(request, 'donate.html')


def map(request):
    regions = Region.objects.all()
    context = {'regions': regions}
    return render(request, 'map.html', context)


def custom404(request, exception):
    return render(request, '404.html', status=404)