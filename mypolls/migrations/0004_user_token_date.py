# Generated by Django 4.0.4 on 2022-04-23 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypolls', '0003_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
