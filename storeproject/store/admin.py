# # coding: utf-8
# from django.contrib import admins
# from store.models import *
#
# class ClothingAdmin(admins.ModelAdmin):
#     list_display = ('brand','name','num',)
#     fieldsets = (
#         ('None',{'fields':('category','name','brand','size','old_price',
#                            'new_price','desc','sales','tag','num','image_url_i',
#                            'image_url_l','image_url_m','image_url_r','image_url_c',)}),
#     )
# admins.site.register(User)
# admins.site.register(Ad)
# admins.site.register(Category)
# admins.site.register(Tag)
# admins.site.register(Size)
# admins.site.register(Brand)
# admins.site.register(Clothing,ClothingAdmin)