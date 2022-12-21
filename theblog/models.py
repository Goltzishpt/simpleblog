from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from slugify import slugify
from PIL import Image
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=15, unique=True, default='')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255)
    profile_pic = ResizedImageField(size=[250, 250], blank=True, null=True,  crop=['top', 'left', 'middle', 'center'], upload_to='images/profile/')
    telegram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    linkedIn_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


# on_delete=models.CASCADE - при удалении пользователя удаляет все его сообщения автоматически
class Post(models.Model):
    title = models.CharField(max_length=30)
    header_image = ResizedImageField(size=[500, 300], blank=True, null=True, upload_to='images/')
    title_tag = models.CharField(max_length=70)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='post', null=True, on_delete=models.SET_NULL)
    snippet = models.CharField(max_length=50, default='Click link above to read blog post')
    likes = models.ManyToManyField(User, related_name='blog_posts')


    def total_likes(self):
        return self.likes.count

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self)
