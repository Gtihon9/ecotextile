from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(upload_to='images', default="images/default.jpg")

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:post_detail', args=[self.slug])

class Image(models.Model):
    image = models.ImageField(upload_to='images', default="images/default.jpg")
    attached_to = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-attached_to__created',)

    def __str__(self):
        return self.attached_to.slug
