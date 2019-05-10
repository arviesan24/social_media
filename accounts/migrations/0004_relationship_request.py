# Generated by Django 2.2 on 2019-04-30 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_request_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='relationships', related_query_name='relationship', to='accounts.Request'),
        ),
    ]
