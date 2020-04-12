import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_complex_sudoers(host):
    f = host.file('/etc/sudoers')

    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o440

    assert f.contains('User_Alias SUPERADMINS = root')
    assert f.contains('Runas_Alias SUPERADMIN = root')
    assert f.contains('Cmnd_Alias SHUTDOWN = /usr/sbin/shutdown')
    assert f.contains(r'+storage SAN= /sbin/umount\*, /sbin/mount\*')
