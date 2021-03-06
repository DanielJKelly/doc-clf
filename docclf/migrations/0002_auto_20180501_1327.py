# Generated by Django 2.0.4 on 2018-05-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docclf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='batch_name',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doc',
            name='file_line_num',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doc',
            name='predicted_class',
            field=models.IntegerField(default=0),
        ),
    ]
