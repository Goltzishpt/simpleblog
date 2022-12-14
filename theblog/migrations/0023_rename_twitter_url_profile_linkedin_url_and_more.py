# Generated by Django 4.1.3 on 2022-12-19 19:26

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0022_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='twitter_url',
            new_name='linkedIn_url',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='website_url',
            new_name='telegram_url',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['top', 'left', 'middle', 'center'], force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[300, 300], upload_to='images/profile/'),
        ),
    ]
