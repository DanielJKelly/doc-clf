# Generated by Django 2.0.4 on 2018-05-02 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docclf', '0002_auto_20180501_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='batch_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
