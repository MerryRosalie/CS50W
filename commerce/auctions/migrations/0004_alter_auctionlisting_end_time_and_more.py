# Generated by Django 4.0 on 2022-01-10 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_auctionlistings_auctionlisting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='winner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='auctions.user'),
        ),
    ]
