# Generated by Django 4.1.3 on 2022-12-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0018_alter_post_title_alter_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=70),
        ),
    ]
