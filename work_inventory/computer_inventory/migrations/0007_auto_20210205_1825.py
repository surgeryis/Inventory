# Generated by Django 3.1.5 on 2021-02-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer_inventory', '0006_auto_20210204_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='computer_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='serial_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
