from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Quote(models.Model):
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name=_('Slug'),
                            help_text=_('A shortname for the quote.'))
    author = models.CharField(blank=True, max_length=255,
                              verbose_name=_('Author'),
                              help_text=_('The quote\'s author'))
    circa = models.CharField(blank=True, max_length=100,
                             verbose_name=_('Circa'),
                             help_text=_('When was the quote created?'))
    quote = models.TextField(verbose_name=_('Quote'))
    image_width = models.IntegerField(blank=True, editable=False)
    image_height = models.IntegerField(blank=True, editable=False)
    image = models.ImageField(verbose_name=_('Image'),
                              upload_to=getattr(settings, 'QUOTES_IMAGE_DIR', 'quotes'),
                              height_field="image_height",
                              width_field="image_width")

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'

    def __unicode__(self):
        return self.slug

    def save(self):
        super(Quote, self).save()
