# Generated by Django 2.0.4 on 2018-05-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docclf', '0004_doc_actual_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='batch_name',
            field=models.CharField(max_length=50),
        ),
    ]
