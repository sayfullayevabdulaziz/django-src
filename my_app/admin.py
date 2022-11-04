from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from .models import Category, Product, Fnksii, Technique, Banner
from django.contrib.admin import AdminSite


class BannerAdminForm(forms.ModelForm):
	description = forms.CharField(
		widget=CKEditorUploadingWidget()
	)

	class Meta:
		model = Banner
		fields = '__all__'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
	form = BannerAdminForm
	prepopulated_fields = {"slug": ("title",)}
	list_display = ['title']



class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}


class TechniqueAdmin(admin.StackedInline):
	model = Technique



class ProductAdmin(admin.ModelAdmin):
	model = Product
	list_display = ['name', 'category']
	prepopulated_fields = {"slug": ("name",)}
	inlines = [TechniqueAdmin]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Fnksii)
# admin.site.register(Technique, TechniqueAdmin)

AdminSite.site_title = 'RadugaZvukov'
AdminSite.site_header = 'RadugaZvukov'
AdminSite.index_title = 'Сайт администрацияси'