# Generated by Django 4.1.2 on 2022-10-31 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_alter_marketitem_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketitem',
            name='ammount',
            field=models.PositiveIntegerField(default=1, verbose_name='Ammount of sets avaliable'),
        ),
    ]
