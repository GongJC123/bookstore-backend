# Generated by Django 2.2.15 on 2020-08-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200811_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='root',
            field=models.BooleanField(default=False, help_text='是否为根分类', verbose_name='是否为根分类'),
        ),
    ]
