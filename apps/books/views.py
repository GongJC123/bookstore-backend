from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from books.models import Category, Books, Comment
from books.serializers import CategorySerializer, BooksSerializer, CommentSerializer


class BooksPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'pageSize'
    # 页码参数
    page_query_param = 'pageNum'
    # 最多能显示多少页
    max_page_size = 100

    # 重写response
    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'data': data,
            # 根据前端要求，把status挪到这里来
            'code': Response.status_code
        })


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

    def category(self, request, pk):
        """查看分类图书列表"""
        books = Books.objects.filter(category=pk).all()
        page_books = self.paginate_queryset(books)

        ser = self.get_serializer(instance=page_books, many=True)

        # return Response(ser.data)
        return self.get_paginated_response(ser.data)

    # @action(methods=['get'], detail=False)
    def search(self, request):
        """ 按书名关键字 搜索 """
        # para = request.GET.get('wd') # django原始方式
        para = request.query_params.get('wd')
        books = Books.objects.filter(title__icontains=para).all()
        page_books = self.paginate_queryset(books)

        ser = self.get_serializer(instance=page_books, many=True)

        return self.get_paginated_response(ser.data)


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


class CommentViewSet(viewsets.ModelViewSet):
    """
    评论
    """
    queryset = Books.objects.all()
    serializer_class = CommentSerializer

    def commentlist(self, request, pk):
        """ 按书名关键字 搜索 """

        comments = Comment.objects.filter(book=pk).all()

        ser = self.get_serializer(instance=comments, many=True)

        return Response(ser.data)
