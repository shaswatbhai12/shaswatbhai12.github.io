# Generated by Django 5.1.6 on 2025-03-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_product_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='services_icons/')),
            ],
        ),
    ]
