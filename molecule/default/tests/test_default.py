import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_users(host):
    assert host.user('newrelic').group == 'newrelic'


def test_packages(host):
    assert host.package('newrelic-infra').is_installed


def test_config(host):
    newrelic_agent_config = host.file(
        '/etc/newrelic-infra.yml'
    )

    assert 'license_key: 123456789123456789123456789123456789' \
        in newrelic_agent_config.content_string
