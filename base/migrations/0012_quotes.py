# Generated by Django 3.2.8 on 2024-02-20 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_vendor_active_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_price', models.CharField(blank=True, max_length=250, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('total_cost', models.CharField(blank=True, max_length=250, null=True)),
                ('item_description', models.TextField(blank=True)),
                ('rfp_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.requestforproposal')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
