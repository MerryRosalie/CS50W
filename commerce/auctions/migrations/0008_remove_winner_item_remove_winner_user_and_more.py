# Generated by Django 4.0 on 2022-01-10 19:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_remove_auctionlisting_winner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='winner',
            name='item',
        ),
        migrations.RemoveField(
            model_name='winner',
            name='user',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='win', to='auctions.user'),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='start_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
        migrations.DeleteModel(
            name='Winner',
        ),
    ]
