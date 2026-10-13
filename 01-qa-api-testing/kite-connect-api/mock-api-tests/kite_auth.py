"""Testable Kite authentication wrapper; no network access without injected client."""

class ConfigurationError(ValueError):
    pass


def create_session(client_factory, api_key, api_secret, request_token):
    """Exchange request token through an injected SDK client, never log secrets."""
    if not all(isinstance(v, str) and v.strip() for v in (api_key, api_secret, request_token)):
        raise ConfigurationError('Missing required Kite authentication configuration')
    client = client_factory(api_key=api_key)
    session = client.generate_session(request_token, api_secret=api_secret)
    if not isinstance(session, dict) or not isinstance(session.get('access_token'), str) or not session['access_token']:
        raise ValueError('Session response did not contain an access token')
    client.set_access_token(session['access_token'])
    return client


def validate_profile(client):
    """Validate session via protected profile API; errors propagate to caller."""
    profile = client.profile()
    if not isinstance(profile, dict) or not profile.get('user_id'):
        raise ValueError('Invalid profile response')
    return True
