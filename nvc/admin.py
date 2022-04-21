from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(FeelingGroup)
admin.site.register(NeedGroup)

# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-models


class FeelingGroupInline(admin.TabularInline):
    model = FeelingGroup.feelings.through
    extra = 0
    verbose_name_plural = 'groups of feelings to which this feeling is a member'


class MetNeedInline(admin.TabularInline):
    model = Need.met_need_feelings.through
    extra = 0
    verbose_name_plural = 'met needs that cause this feeling'


class UnmetNeedInline(admin.TabularInline):
    model = Need.unmet_need_feelings.through
    extra = 0
    verbose_name_plural = 'unmet needs that cause this feeling'


class PoemInline(admin.TabularInline):
    model = Poem.feelings.through
    extra = 0
    verbose_name_plural = 'poems with this feeling'


class FeelingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'poems',
        'needs_met_count',
        'needs_unmet_count',
    )
    inlines = [
        FeelingGroupInline,
        MetNeedInline,
        UnmetNeedInline,
        PoemInline,
    ]


class FeelingGroupAdmin(admin.ModelAdmin):
    inlines = [FeelingGroupInline, ]
    exclude = ('feelings',)


class NeedAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'poems',
        'met_need_feelings_count',
        'unmet_need_feelings_count',
    )


class PoemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'feelings_count',
        # 'needs_count',
    )


# Register the admin class ith the associated model
admin.site.register(Feeling, FeelingAdmin)
admin.site.register(Need, NeedAdmin)
admin.site.register(Poem, PoemAdmin)
