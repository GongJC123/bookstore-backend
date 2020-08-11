from datetime import datetime

from django.db import models

from users.models import UserProfile


class Category(models.Model):

    name = models.CharField("类别名称", default="", max_length=30, help_text="类别名")
    root = models.BooleanField("是否为根分类", default=True, help_text="是否为根分类")
    parentId = models.ForeignKey('self', verbose_name="父级分类id", blank=True, null=True, on_delete=models.CASCADE)
    # related_name = "sub_cat

    class Meta:
        verbose_name = "图书分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Books(models.Model):

    title = models.CharField("书籍名称", max_length=100, help_text="书籍名称")
    author = models.CharField('作者', max_length=30, help_text='作者')
    price = models.FloatField('价格', default=0, help_text='市场价格')
    discount = models.FloatField('折扣', default=1, help_text='折扣')
    imgUrl = models.ImageField('图片', upload_to='books/images/', null=True, blank=True, help_text='图片')
    bigImgUrl = models.ImageField('大图', upload_to='books/images/big/', null=True, blank=True, help_text='大图')
    bookConcern = models.CharField('出版社', max_length=100, help_text='出版社')
    publishDate = models.DateField('出版日期', blank=True, null=True, help_text='出版日期')
    brief = models.CharField('简介', max_length=200, blank=True, null=True, help_text='简介')
    inventory = models.IntegerField('库存', default=0, help_text='库存')
    detail = models.TextField('详情', default='', blank=True, null=True, help_text='详情')
    newness = models.BooleanField('是否新品', default=False, help_text='是否新品')
    hot = models.BooleanField('是否热销', default=False, help_text='是否热销')
    specialOffer = models.BooleanField('特别优惠', default=False, help_text='特别优惠')
    slogan = models.CharField('标语', max_length=200, blank=True, null=True, help_text='标语')
    category = models.ForeignKey(Category, verbose_name='图书分类', blank=True, null=True,
                                 on_delete=models.CASCADE, help_text='图书分类')

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):

    content = models.TextField('评论内容', default='', help_text='评论内容')
    commentDate = models.DateTimeField('评论时间', default=datetime.now)
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户外键')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='图书外键')

    class Meta:
        verbose_name = '图书评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
