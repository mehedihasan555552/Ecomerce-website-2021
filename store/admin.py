from django.contrib import admin
from . models import *
from django.utils.html import format_html
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1



class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('product_name',)}
    list_display = ('product_name','price','stock','category','modified_date','is_available',)
    inlines = [ProductGalleryInline]



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('category_name',)}
    list_display = ('category_name','slug')

class VariationAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active')
    list_editable=('is_active',)
    list_filter = ('product','variation_category','variation_value','is_active',)


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields=('payment','user','product','quantity','product_price','ordered')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number','first_name','last_name','email','phone','city','order_total','tax','status','is_ordered','created_at']
    list_filter = ['status','is_ordered']
    search_fields = ['order_number','first_name','last_name','phone','email']
    list_per_page = 20 
    inlines = [OrderProductInline]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Variation,VariationAdmin)


admin.site.register(Payment)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct)

admin.site.register(ReviewRating)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('thumbnail','user','city','state','country')
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_pic.url))
        thumbnail.short_description ='Profile Picture'
        

admin.site.register(UserProfile,UserProfileAdmin)






admin.site.register(ProductGallery)