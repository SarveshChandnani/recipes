# Generated by Django 3.2.4 on 2021-06-15 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cookbook', '0134_space_allow_sharing'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='space',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.space'),
        ),
        migrations.AddField(
            model_name='nutritioninformation',
            name='space',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.space'),
        ),
        migrations.AddField(
            model_name='step',
            name='space',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.space'),
        ),

    ]