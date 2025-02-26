# Generated by Django 3.2.8 on 2021-11-08 16:38

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('LegacySite', '0002_encryptedcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='amount',
            field=django_cryptography.fields.encrypt(models.IntegerField()),
        ),
        migrations.AlterField(
            model_name='card',
            name='data',
            field=django_cryptography.fields.encrypt(models.BinaryField(unique=True)),
        ),
        migrations.AlterField(
            model_name='card',
            name='fp',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=100, unique=True)),
        ),
        migrations.DeleteModel(
            name='Encryptedcard',
        ),
    ]
