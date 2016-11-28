from django.db import models
import datetime

# Create your models here.


class Project(models.Model):

    YEAR_CHOICES = [(str(r), str(r)) for r in range(2006, datetime.date.today().year+1)]

    class Meta(object):
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Name"
    )

    main_image = models.ImageField(
        blank=True,
        verbose_name="Image",
        null=True
    )

    year = models.CharField(
        max_length=4,
        verbose_name="Year",
        blank=True,
        choices=YEAR_CHOICES,
    )

    info = models.TextField(
        blank=True,
        verbose_name="Info",
        default=''
    )

    def __str__(self):
        return "{}".format(self.name)


class Image(models.Model):

    class Meta(object):
        verbose_name = "Image"
        verbose_name_plural = "Images"

    image = models.ImageField(
        blank=True,
        verbose_name="Image",
        null=True
    )

    project = models.ForeignKey(Project)

    def __str__(self):
        return "{}".format(self.project)


class About(models.Model):

    class Meta(object):
        verbose_name = "About"
        verbose_name_plural = "About"

    photo = models.ImageField(
        blank=True,
        verbose_name="Photo",
        null=True
    )

    info = models.TextField(
        blank=True,
        verbose_name="Info",
        default=''
    )