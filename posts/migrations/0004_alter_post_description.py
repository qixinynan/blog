# Generated by Django 4.1.4 on 2023-01-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, help_text='留空则自动截取文章前120个字符', max_length=120, verbose_name='文章描述'),
        ),
    ]
