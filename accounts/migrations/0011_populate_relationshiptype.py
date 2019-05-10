from django.db import migrations, models


def populate_name(apps, schema_editor):

    RelationshipType = apps.get_model('accounts', 'RelationshipType')
    name_list = ['friend', 'in a relationship', 'blocked']

    for item in name_list:
        relationship_type = RelationshipType(name=item)
        relationship_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190430_1344'),
    ]

    operations = [
        migrations.RunPython(
            populate_name, reverse_code=migrations.RunPython.noop),
    ]
