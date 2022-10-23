# Generated by Django 4.1.2 on 2022-10-15 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import marketplace.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_legosetimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='Selling price')),
                ('currency', models.CharField(choices=[('USD', '$'), ('EUR', '€')], max_length=150)),
                ('lego_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.legoset', verbose_name='LEGO set')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Seller')),
            ],
        ),
        migrations.CreateModel(
            name='MarketItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=marketplace.utils.market_item_image_filepath, verbose_name='Item Image')),
                ('market_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.marketitem')),
            ],
        ),
    ]