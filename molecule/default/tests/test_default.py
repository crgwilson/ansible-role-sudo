import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# TODO: Add more tests & scenarios
def test_default_packages(host):
    p = host.package('sudo')
    assert p.is_installed
