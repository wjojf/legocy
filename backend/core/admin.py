from http.cookiejar import LoadError
from django.contrib import admin
from .models import LegoSeries, LegoSet, LegoSetImage

# Register your models here
admin.site.register(LegoSeries)
admin.site.register(LegoSetImage)

class LegoSetImageInline(admin.StackedInline):
    model = LegoSetImage
    extra = 1
    classes = ['wide', 'extrapretty']


@admin.register(LegoSet)
class LegoSetAdmin(admin.ModelAdmin):
    inlines = [LegoSetImageInline]
    search_fields = ['set_number', 'title']
    fieldsets = (
      ('Set info', {
          'fields': (
                'set_number',
                'series',
                'title',
                'n_details'
            )
      }),
    )

