# Generated by Django 3.2.16 on 2022-11-21 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_listings_bathrooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='bathrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listings',
            name='bedrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listings',
            name='last_sold_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listings',
            name='link',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='listings',
            name='property_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listings',
            name='rent_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listings',
            name='rentzestimate_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listings',
            name='tax_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listings',
            name='zestimate_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listings',
            name='zillow_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listings',
            name='zipcode',
            field=models.IntegerField(default=0),
        ),
    ]