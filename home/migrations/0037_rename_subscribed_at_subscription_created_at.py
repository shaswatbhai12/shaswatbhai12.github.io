# Generated by Django 5.1.6 on 2025-03-16 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='subscribed_at',
            new_name='created_at',
        ),
    ]
