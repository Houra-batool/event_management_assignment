from django.conf import settings


def allauth_settings(request):
    #Expose some settings from django-allauth in template
    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
    }
