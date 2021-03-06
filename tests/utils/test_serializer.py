import builtins
from maestral.utils.serializer import error_to_dict


def test_error_to_dict():
    from requests.exceptions import RequestException
    from maestral.errors import SyncError

    exc1 = RequestException('test error')
    exc2 = SyncError('test', 'test')

    serialized_excs = [error_to_dict(exc) for exc in (exc1, exc2)]

    default_keys = ('type', 'inherits', 'traceback', 'title', 'message')

    for serialized_exc in serialized_excs:
        assert all(isinstance(key, str) for key in serialized_exc.keys())
        assert all(type(val).__name__ in dir(builtins) for val in serialized_exc.values())
        assert all(key in serialized_exc for key in default_keys)
