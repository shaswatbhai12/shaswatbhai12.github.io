# Generated by Django 5.1.6 on 2025-03-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_quickenquiry_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quickenquiry',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='quickenquiry',
            name='mobile_number',
            field=models.CharField(max_length=15),
        ),
    ]
