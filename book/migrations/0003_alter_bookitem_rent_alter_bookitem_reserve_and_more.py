# Generated by Django 4.0.4 on 2022-05-27 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0002_alter_bookitem_rent_alter_bookitem_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='rent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='reserve',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserve', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b731e5d8-00d4-4121-82be-5e4fc34741f9'), editable=False),
        ),
    ]
