from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from books.models import Category, Books
from books.serializers import CategorySerializer, BooksSerializer


class BooksPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'pageSize'
    #页码参数
    page_query_param = 'pageNum'
    #最多能显示多少页
    max_page_size = 100


class CategoryViewSet(viewsets.ModelViewSet):
    """
    图书分类
    """
    queryset = Category.objects.filter(root=True).all()
    serializer_class = CategorySerializer


class BooksViewSet(viewsets.ModelViewSet):
    """
    所有图书列表
    id图书详情
    """
    queryset = Books.objects.filter(hot=True).all()
    serializer_class = BooksSerializer
    pagination_class = BooksPagination

    # @action(methods=['get'], detail=False, url_path='category/<pk>')
    # def category(self, request, pk):
    #     """查看最新成立的部门"""
    #     print('pk--------------', pk)
    #     books = Books.objects.filter(category=pk).all()
    #     serializer = self.get_serializer(instance=books)
    #     return Response(serializer.data)


class NewBooksViewSet(viewsets.ModelViewSet):
    """
    新书列表
    """
    queryset = Books.objects.filter(newness=True).all()
    serializer_class = BooksSerializer


class HotBooksViewSet(viewsets.ModelViewSet):
    """
    热门书籍
    """
    queryset = Books.objects.filter(hot=True).all()
    serializer_class = BooksSerializer
