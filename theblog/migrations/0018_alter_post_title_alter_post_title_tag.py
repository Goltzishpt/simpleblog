# Generated by Django 4.1.3 on 2022-12-14 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0017_alter_category_name_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=50),
        ),
    ]
