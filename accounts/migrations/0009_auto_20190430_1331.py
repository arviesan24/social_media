# Generated by Django 2.2 on 2019-04-30 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_relationshiptype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relationships', related_query_name='relationship', to='accounts.RelationshipType'),
        ),
    ]
