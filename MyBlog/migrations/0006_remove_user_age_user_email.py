# Generated by Django 4.2.13 on 2024-06-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0005_post_modified_date_post_publish_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=True, max_length=254),
        ),
    ]
