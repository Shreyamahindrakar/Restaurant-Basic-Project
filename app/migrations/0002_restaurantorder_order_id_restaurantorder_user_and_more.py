# Generated by Django 5.1.2 on 2024-10-28 03:44

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantorder',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='restaurantorder',
            name='user',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurantorder',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
