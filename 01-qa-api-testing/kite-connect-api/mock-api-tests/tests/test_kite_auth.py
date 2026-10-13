from unittest.mock import Mock
import pytest
from kite_auth import ConfigurationError, create_session, validate_profile

API_KEY = 'FAKE_KEY'
API_SECRET = 'FAKE_SECRET'
REQUEST_TOKEN = 'FAKE_REQUEST_TOKEN'


def factory_with(session=None, side_effect=None):
    client = Mock()
    if side_effect is not None:
        client.generate_session.side_effect = side_effect
    else:
        client.generate_session.return_value = {'access_token': 'FAKE_ACCESS_TOKEN'} if session is None else session
    return Mock(return_value=client), client


def test_successful_exchange_sets_access_token():
    factory, client = factory_with()
    result = create_session(factory, API_KEY, API_SECRET, REQUEST_TOKEN)
    assert result is client
    factory.assert_called_once_with(api_key=API_KEY)
    client.generate_session.assert_called_once_with(REQUEST_TOKEN, api_secret=API_SECRET)
    client.set_access_token.assert_called_once_with('FAKE_ACCESS_TOKEN')


@pytest.mark.parametrize('values', [('', API_SECRET, REQUEST_TOKEN), (API_KEY, '', REQUEST_TOKEN), (API_KEY, API_SECRET, ''), (None, API_SECRET, REQUEST_TOKEN)])
def test_missing_configuration(values):
    factory, client = factory_with()
    with pytest.raises(ConfigurationError, match='Missing required'):
        create_session(factory, *values)
    factory.assert_not_called()


@pytest.mark.parametrize('response', [{}, {'access_token': ''}, {'access_token': None}, {'access_token': 123}])
def test_invalid_session_response(response):
    factory, client = factory_with(response)
    with pytest.raises(ValueError, match='did not contain'):
        create_session(factory, API_KEY, API_SECRET, REQUEST_TOKEN)
    client.set_access_token.assert_not_called()


@pytest.mark.parametrize('error', [ValueError('invalid request token'), ValueError('expired request token'), PermissionError('bad checksum')])
def test_exchange_rejections_propagate(error):
    factory, client = factory_with(side_effect=error)
    with pytest.raises(type(error)):
        create_session(factory, API_KEY, API_SECRET, REQUEST_TOKEN)
    client.set_access_token.assert_not_called()


def test_valid_profile():
    client = Mock()
    client.profile.return_value = {'user_id': 'DEMO_USER'}
    assert validate_profile(client) is True
    client.profile.assert_called_once_with()


@pytest.mark.parametrize('response', [{}, None, {'user_id': ''}])
def test_invalid_profile_response(response):
    client = Mock()
    client.profile.return_value = response
    with pytest.raises(ValueError, match='Invalid profile'):
        validate_profile(client)


@pytest.mark.parametrize('error', [PermissionError('expired token'), ConnectionError('network unavailable')])
def test_profile_errors_propagate(error):
    client = Mock()
    client.profile.side_effect = error
    with pytest.raises(type(error)):
        validate_profile(client)
