from django.db import migrations, models


def populate_status(apps, schema_editor):

    Request = apps.get_model('accounts', 'Request')
    status_list = ['pending', 'confirmed']

    for item in status_list:
        request = Request(status=item)
        request.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190430_1005'),
    ]

    operations = [
        migrations.RunPython(
            populate_status, reverse_code=migrations.RunPython.noop),
    ]
