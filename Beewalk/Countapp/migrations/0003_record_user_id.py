# Generated by Django 5.0.3 on 2024-06-30 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accountapp', '0002_member_last_login'),
        ('Countapp', '0002_record_msec'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Accountapp.member'),
        ),
    ]
