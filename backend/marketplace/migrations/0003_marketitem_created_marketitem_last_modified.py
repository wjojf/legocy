# Generated by Django 4.1.2 on 2022-10-15 15:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_marketitem_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marketitem',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]