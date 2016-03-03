import requests
from django.conf import settings


def check_token(access_token):
    """ Check a user's UUID token if social auth is enabled
    :param access_token: The user's OAuth token
    :return: The user's email address if the token is valid, or a default one if social auth is disabled
    """
    if settings.SOCIAL_AUTH_PEBBLE_ROOT_URL:
        if not access_token:
            return False
        else:
            url = '{0}/api/v1/me.json'.format(settings.SOCIAL_AUTH_PEBBLE_ROOT_URL)
            result = requests.get(url, headers={'Authorization': 'Bearer {0}'.format(access_token)})
            try:
                result.raise_for_status()
            except:
                return False
            return result.json()['email']
    else:
        return "cloudpebble@pebble.com"