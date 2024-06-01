# Generated by Django 4.2.13 on 2024-06-01 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0004_remove_post_modified_date_remove_post_publish_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]
