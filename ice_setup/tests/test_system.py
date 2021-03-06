import os
import tempfile
from pytest import raises
import pytest
from textwrap import dedent
from ice_setup.ice import get_fqdn, ICEError, DirNotFound


class FakeSocket(object):
    pass


@pytest.fixture
def cephdeploy_conf():
    path = tempfile.mkstemp()

    def fin():
        os.remove(path)

    return path[-1]


class TestGetFQDN(object):

    def setup(self):
        self.sock = FakeSocket()

    def test_dot_local_fqdn(self):
        self.sock.getfqdn = lambda: 'alfredo.local'
        assert get_fqdn(_socket=self.sock) is None

    def test_localhost(self):
        self.sock.getfqdn = lambda: 'localhost'
        assert get_fqdn(_socket=self.sock) is None

    def test_valid_fqdn(self):
        self.sock.getfqdn = lambda: 'zombo.com'
        assert get_fqdn(_socket=self.sock) == 'zombo.com'
