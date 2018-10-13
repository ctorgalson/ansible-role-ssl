import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("path,user,group,mode", [
    ("/etc/ssl/certs", "root", "root", "0755"),
    ("/etc/ssl/private", "root", "root", "0700"),
    ("/etc/ssl/certs/www.example.com.key", "root", "root", "0600"),
    ("/etc/ssl/certs/www.example.com.crt", "root", "root", "0644"),
    ("/etc/ssl/self/certs", "root", "root", "0755"),
    ("/etc/ssl/self/private", "root", "root", "0755"),
    ("/etc/ssl/self/certs/www.example.com-key.pem", "root", "root", "0600"),
    ("/etc/ssl/self/certs/www.example.com-crt.pem", "root", "root", "0644"),
    ("/etc/ssl/self/private/www.example.com.csr", "root", "root", "0644"),
])
def test_ssl_files_and_directories(host, path, user, group, mode):
    f = host.file(path)

    assert f.exists
    assert f.user == user
    assert f.group == group
    assert oct(f.mode) == mode
