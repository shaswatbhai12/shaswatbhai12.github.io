# Generated by Django 5.1.6 on 2025-03-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_rename_created_at_contact_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default='No message provided', max_length=1000),
        ),
        migrations.AddField(
            model_name='contact',
            name='pincode',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
