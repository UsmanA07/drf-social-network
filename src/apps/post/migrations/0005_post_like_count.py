# Generated by Django 5.1.6 on 2025-05-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
