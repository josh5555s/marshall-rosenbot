from django.db import models
# from django.db.models import Sum


class Feeling(models.Model):
    name = models.CharField('name', max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def etymology_link(self):
        return f'https://www.etymonline.com/search?q={self.name}'

    def poems(self):
        feeling = Feeling.objects.get(id=self.id)
        poem_list = feeling.poem_set.all()
        return poem_list.count()

    def needs_met_list(self):
        return Need.objects.filter(met_need_feelings__name=self.name)

    def needs_met_count(self):
        return Need.objects.filter(met_need_feelings__name=self.name).count()

    def needs_unmet_list(self):
        return Need.objects.filter(unmet_need_feelings__name=self.name)

    def needs_unmet_count(self):
        return Need.objects.filter(unmet_need_feelings__name=self.name).count()

    def __str__(self):
        return self.name


class FeelingGroup(models.Model):
    name = models.CharField('name', max_length=200, unique=True)
    feelings = models.ManyToManyField(Feeling)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Need(models.Model):
    name = models.CharField('name', max_length=200, unique=True)
    met_need_feelings = models.ManyToManyField(
        Feeling, related_name='met_feelings')
    unmet_need_feelings = models.ManyToManyField(
        Feeling, related_name='unmet_feelings')

    def poems(self):
        need = Need.objects.get(id=self.id)
        poem_list = need.poem_set.all()
        return poem_list.count()

    def met_need_feelings_count(self):
        return self.met_need_feelings.count()

    def unmet_need_feelings_count(self):
        return self.unmet_need_feelings.count()

    class Meta:
        ordering = ['name']

    def etymology_link(self):
        return f'https://www.etymonline.com/search?q={self.name}'

    def __str__(self):
        return self.name


class NeedGroup(models.Model):
    name = models.CharField('name', max_length=200, unique=True)
    needs = models.ManyToManyField(Need)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Poem(models.Model):
    title = models.CharField('title', max_length=200)
    poem = models.TextField('poem')
    feelings = models.ManyToManyField(Feeling)
    needs = models.ManyToManyField(Need)

    def feelings_count(self):
        return self.feelings.count()

    def needs_count(self):
        return self.needs.count()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
