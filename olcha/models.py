from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/images/')
    slug = models.SlugField(unique=True,null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True
    )

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} => {self.parent.title}"
        return self.title

    class Meta:
        verbose_name_plural = 'categories'

