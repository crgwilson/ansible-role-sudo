import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_default_packages(host):
    p = host.package('sudo')
    assert p.is_installed


def test_default_sudoers(host):
    f = host.file('/etc/sudoers')

    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o440

    defaults = [
        '!visiblepw',
        'always_set_home',
        'match_group_by_gid',
        'always_query_group_plugin',
        'env_reset',
        'env_keep =  "COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS"',
        'env_keep += "MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE"',
        'env_keep += "LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES"',  # noqa E501
        'env_keep += "LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE"',
        'env_keep += "LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY"',  # noqa E501
        'secure_path = /sbin:/bin:/usr/sbin:/usr/bin'
    ]
    for d in defaults:
        assert f.contains('Defaults ' + d)

    assert f.contains('root ALL=(ALL:ALL) ALL')

    if host.system_info.distribution == 'debian':
        assert f.contains('%sudo ALL=(ALL:ALL) ALL')
    else:
        assert f.contains('%wheel ALL=(ALL:ALL) ALL')

    assert f.contains('#includedir /etc/sudoers.d')
