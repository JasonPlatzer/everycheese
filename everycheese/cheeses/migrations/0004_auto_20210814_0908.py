# Generated by Django 3.1.1 on 2021-08-14 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cheeses', '0003_auto_20210814_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cheese',
            name='firmness',
            field=models.CharField(choices=[('unspecified', 'Unspecified'), ('soft', 'Soft'), ('semi-soft', 'Semi-Soft'), ('semi-hard', 'Semi-Hard'), ('hard', 'Hard')], default='unspecified', max_length=44, verbose_name='Firmness'),
        ),
    ]
