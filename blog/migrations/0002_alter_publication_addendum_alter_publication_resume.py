# Generated by Django 5.0.1 on 2024-01-14 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='addendum',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='resume',
            field=models.CharField(max_length=100),
        ),
    ]
