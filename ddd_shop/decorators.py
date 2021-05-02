from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def attendant_only(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    """
     Decorator for view to check id user is an attendant

    """

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_attendant,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def owner_only(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    """
     Decorator for view to check id user is a store owner

    """

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_owner,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
