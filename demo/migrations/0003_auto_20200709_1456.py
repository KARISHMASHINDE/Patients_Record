# Generated by Django 3.0.8 on 2020-07-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200709_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='he_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
