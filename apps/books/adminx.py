# Register your models here.

import xadmin
from .models import Books, Category, Comment


class BooksAdmin(object):
    # 显示的列
    list_display = ["title", "author", "price", "discount", "bookConcern", "publishDate",
                    "inventory", "newness", "hot", "slogan"]
    # 可以搜索的字段
    search_fields = ['name', ]
    # 列表页可以直接编辑的
    list_editable = ["newness", 'hot', ]
    # 过滤器
    list_filter = ["title", "author", "price", "discount", "bookConcern", "publishDate",
                   "inventory", "newness", "hot", "category__name"]

    # 在添加商品的时候可以添加商品图片
    # class GoodsImagesInline(object):
    #     model = GoodsImage
    #     exclude = ["add_time"]
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [GoodsImagesInline]


class CategoryAdmin(object):
    list_display = ["name", "root", "parentId"]
    list_filter = ["name", "root", "parentId"]
    search_fields = ['name', ]


class CommentAdmin(object):
    list_display = ["username", "book", "content", 'commentDate']
    list_filter = ["username", "book", "commentDate"]
    search_fields = ['book', 'username']


xadmin.site.register(Books, BooksAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Comment, CommentAdmin)

