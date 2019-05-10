from django.db import migrations, models
from django.utils.text import slugify


def populate_slug(apps, schema_editor):

    Profile = apps.get_model('accounts', 'Profile')
    profile_list = Profile.objects.all()

    for item in profile_list:
        slug_username = slugify(item.user.username)
        str_id = str(item.user.id)
        item.slug = f'{slug_username}-{str_id}'
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_slug'),
    ]

    operations = [
        migrations.RunPython(
            populate_slug, reverse_code=migrations.RunPython.noop),
    ]
