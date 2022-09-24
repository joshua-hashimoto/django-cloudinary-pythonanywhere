from functools import reduce
import itertools
import operator

from django.db import models
from django.db.models import Q
from django.urls import reverse

from core.additional.models import CoreModel


class WebsiteQuerySet(models.QuerySet):

    def actives(self):
        return self.filter(is_active=True)

    def in_actives(self):
        return self.filter(is_active=False)

    def search(self, query):
        query_split = [i.split(",") for i in query.split(" ")]
        query_list = list(itertools.chain.from_iterable(query_split))
        query_filtered_list = [i for i in query_list if i != ""]
        lookup = reduce(operator.or_, (Q(is_active=True) & Q(title__icontains=option) for option in query_filtered_list))
        return self.filter(lookup)


class WebsiteManager(models.Manager):

    def get_queryset(self):
        return WebsiteQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def in_actives(self):
        return self.get_queryset().in_actives()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Website(CoreModel):
    title = models.CharField(max_length=128)
    url = models.URLField()

    objects = WebsiteManager()

    class Meta:
        verbose_name = "WEBサイト"
        verbose_name_plural = "WEBサイト"
        ordering = ("-timestamp", )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("website:detail", kwargs={"pk": self.pk})


class SnapQueryset(models.QuerySet):

    def actives(self):
        return self.filter(is_active=True)

    def in_actives(self):
        return self.filter(is_active=False)


class SnapManager(models.Manager):

    def get_queryset(self):
        return SnapQueryset(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def in_actives(self):
        return self.get_queryset().in_actives()


def upload_image_to(instance, filename):
    asset_path = f"{str(instance.website.title)}/{filename}"
    return asset_path


class Snap(CoreModel):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name="snaps")
    snap = models.ImageField(upload_to=upload_image_to)

    objects = SnapManager()

    class Meta:
        verbose_name = "スナップショット"
        verbose_name_plural = "スナップショット"

    def __str__(self):
        return self.get_filename()

    def get_filename(self):
        return self.snap.name.split("/")[-1]
