# Generated by Django 4.0.4 on 2022-04-23 16:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mypolls', '0005_alter_user_token_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 16, 49, 0, 137633, tzinfo=utc)),
        ),
    ]
