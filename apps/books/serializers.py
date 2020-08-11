# author: GongJichao
# createTime: 2020/8/11 20:04
from abc import ABC

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from books.models import Category, Books


class CategorySerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=60)
    root = serializers.BooleanField()
    parentId = serializers.IntegerField(source='parentId.id', allow_null=True)
    children = serializers.ListField(source='get_children_categories', child=RecursiveField())

    class Meta:
        model = Category


class BooksSerializer(serializers.ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Books
        fields = '__all__'


# class BookCategorySerializer(serializers.ModelSerializer):
#
#     Category = CategorySerializer()
#
#     class Meta:
#         model = Books


