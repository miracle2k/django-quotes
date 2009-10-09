from django.db import models

class Quote(models.Model):
    slug = models.SlugField(max_length=255, unique=True, help_text='A shortname for the quote.')
    author = models.CharField(blank=True, max_length=255, help_text='The quote\'s author')
    circa = models.CharField(blank=True, max_length=100, help_text="When was the quote created?")
    quote = models.TextField()
    image_width = models.IntegerField(blank=True, editable=False)
    image_height = models.IntegerField(blank=True, editable=False)
    image = models.ImageField(upload_to='django-quotes', height_field="image_height", width_field="image_width")

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'

    def __unicode__(self):
        return self.slug

    def save(self):
        super(Quote, self).save()
