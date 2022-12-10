# Generated by Django 4.0 on 2022-01-10 18:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_category_alter_auctionlisting_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='start_bid',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='start_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categorized_item', to='auctions.category'),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=32),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.auctionlisting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bidder', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.user')),
                ('item', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_bidded', to='auctions.auctionlisting')),
            ],
        ),
    ]