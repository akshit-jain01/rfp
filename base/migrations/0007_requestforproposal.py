# Generated by Django 3.2.8 on 2024-02-18 12:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestForProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=250)),
                ('rfp_no', models.CharField(max_length=250)),
                ('quantity', models.IntegerField(default=0)),
                ('last_date', models.DateField()),
                ('minimum_price', models.FloatField(max_length=250)),
                ('maximum_price', models.FloatField(max_length=250)),
                ('item_description', models.TextField()),
                ('categories', models.ManyToManyField(related_name='category', to='base.Category')),
                ('vendor', models.ManyToManyField(related_name='vendor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]