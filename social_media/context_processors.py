"""Project wide custom context processors."""

from django.conf import settings


def global_template_variables(request):
    """Returns custom context processors."""

    return {
        'API_ROOT_URL': settings.API_ROOT_URL,
    }
