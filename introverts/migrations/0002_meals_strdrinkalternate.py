# Generated by Django 4.0.3 on 2022-05-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introverts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='strDrinkAlternate',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
