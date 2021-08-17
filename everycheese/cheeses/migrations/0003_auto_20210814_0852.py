# Generated by Django 3.1.1 on 2021-08-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0002_cheese_country_of_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheese',
            name='firmness',
            field=models.CharField(choices=[('unspecified', 'Unspecified'), ('soft', 'Soft'), ('semi-soft', 'Semi-Soft'), ('semi-hard', 'Semi-Hard'), ('hard', 'Hard'), ('<django.db.models.fields.related.ForeignKey>', 'Creator')], default='unspecified', max_length=44, verbose_name='Firmness'),
        ),
    ]