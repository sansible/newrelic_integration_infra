# NewRelic Infra Integration

Master: [![Build Status](https://travis-ci.org/sansible/newrelic_integration_infra.svg?branch=master)](https://travis-ci.org/sansible/newrelic_integration_infra)
Develop: [![Build Status](https://travis-ci.org/sansible/newrelic_integration_infra.svg?branch=develop)](https://travis-ci.org/sansible/newrelic_integration_infra)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

Installs New Relic's system metrics integration and configures an INI file with
settings. Comes with default settings that setup license key, log levels and
instance labels.

By default the start_on_boot flag for this integration is not enabled on boot,
in addition to allowing you to enable the service per environment you can also
start the service elsewhere once an instance has finished booting. The intention
here is to prevent false alerts triggered by the high saturation encountered
during OS boot.




## Installation and Dependencies

To install run `ansible-galaxy install sansible.newrelic_integration_infra` or add this to your
`roles.yml`.

```YAML
- name: sansible.newrelic_integration_infra
  version: v1.0.0-latest
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses tags: **build** and **configure**

* `build` - Installs New Relic Infra integrations
* `configure` - Configures New Relic, requires a valid license key




## Examples

### The start_on_boot flag

The start_on_boot flag will start the integration and write any required
config files, executed via the configure tag. This tag can be used for
activating an integration on a per environment basis.

```YAML
- name: Install and configure newrelic
  hosts: "somehost"

  roles:
    - role: sansible.newrelic_integration_infra
      sansible_newrelic_integrations_infra_start_on_boot: yes
      sansible_newrelic_integration_infra_settings:
        license_key: 123456789123456789123456789123456789
        custom_attributes:
          org: sansible
          role: newrelic
```
