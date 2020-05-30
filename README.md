# Ansible role: Sudo

![Molecule Test](https://github.com/crgwilson/ansible-role-sudo/workflows/Molecule%20Test/badge.svg)

Manage the sudoers file on linux hosts

* Install sudo packages
* Generate the sudoers file from a jinja2 template


## Variables

### `sudo_user_aliases` - list(dict)

Define user aliases to be used later in the sudoers file

| Key | Type | Description |
| --- | ---- | ----------- |
| alias | `str` | The name of the user alias to create |
| users | `list` | The users to alias |

Example:
```yaml
sudo_user_aliases:
  - alias: SYSADMINS
    users:
      - bob
      - jim
      - frank
```

### `sudo_runas_aliases` - list(dict)

Define RunAs aliases to be used later in the sudoers file

| Key | Type | Description |
| --- | ---- | ----------- |
| alias | `str` | The name of the user alias to create |
| users | `list` | The users to alias |

Example:
```yaml
sudo_user_runas_aliases:
  - alias: OPERATOR
    users:
      - root
      - operator
```

### `sudo_host_aliases` - list(dict)

Define host aliases to be used later in the sudoers file

| Key | Type | Description |
| --- | ---- | ----------- |
| alias | `str` | The name of the user alias to create |
| hosts | `list` | The hosts to alias |

Example:
```yaml
sudo_host_aliases:
  - alias: WEB
    hosts:
      - apache-01
      - nginx-01
```

### `sudo_cmnd_aliases` - list(dict)

Define command aliases to be used later in the sudoers file

| Key | Type | Description |
| --- | ---- | ----------- |
| alias | `str` | The name of the user alias to create |
| commands | `list` | The commands to alias |

Example:
```yaml
sudo_cmnd_aliases:
  - alias: REBOOT
    commands:
      - /usr/sbin/shutdown
```

### `sudo_defaults` - list(str)

Override default configuration

Example:
```yaml
sudo_defaults:
  - env_reset
  - mail_badpass
  - secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
```

### `sudo_users` - list(dict)

Define sudo user privileges

| Key | Type | Required | Default | Description |
| --- | ---- | -------- | ------- | ----------- |
| name | `str` | Y | N/A | The name of the user |
| hosts | `str` | Y | N/A | The hosts where the user is allowed to run sudo |
| runas | `str` | N | `''` | Users and/or groups commands can be run as |
| nopasswd | `bool` | N | `False` | Whether or not to apply `NOPASSWD` to the created spec |
| commands | `list(str)` | Y | N/A | Each command the user will be allowed to run with sudo |

Example:
```yaml
sudo_users:
  - name: root
    hosts: ALL
    runas: ALL
    commands:
      - ALL
  - name: bob
    hosts: +bobland  # every host in the bobland netgroup
    nopasswd: true
    commands:
      - /usr/bin/su wildfly
```

### `sudo_groups` - list(dict)

Define sudo group privileges

| Key | Type | Required | Default | Description |
| --- | ---- | -------- | ------- | ----------- |
| name | `str` | Y | N/A | The name of the group |
| hosts | `str` | Y | N/A | The hosts where the group is allowed to run sudo |
| runas | `str` | N | `''` | Users and/or groups commands can be run as |
| nopasswd | `bool` | N | `False` | Whether or not to apply `NOPASSWD` to the created spec |
| commands | `list(str)` | Y | N/A | Each command the users within the group will be allowed to run with sudo |

Example:
```yaml
sudo_groups:
  - name: wheel
    hosts: ALL
    runas: ALL
    commands:
      - ALL
  - name: ssh_admins
    hosts: ALL
    runas: ALL
    nopasswd: true
    commands:
```

### `sudo_netgroups` - list(dict)

Define sudo netgroup privileges

| Key | Type | Required | Default | Description |
| --- | ---- | -------- | ------- | ----------- |
| name | `str` | Y | N/A | The name of the netgroup |
| hosts | `str` | Y | N/A | The hosts where the netgroup is allowed to run sudo |
| runas | `str` | N | `''` | Users and/or groups commands can be run as |
| nopasswd | `bool` | N | `False` | Whether or not to apply `NOPASSWD` to the created spec |
| commands | `list(str)` | Y | N/A | Each command the users within the netgroup will be allowed to run with sudo |

Example:
```yaml
sudo_netgroups:
  - name: storage
    hosts: SAN
    commands:
      - /sbin/umount*
      - /sbin/mount*
```

### `sudo_include` - list(dict)

Other files to include in the sudoers file

| Key | Type | Required | Default | Description |
| --- | ---- | -------- | ------- | ----------- |
| path | `str` | Y | N/A | The path to the file or directory to include |
| is_dir | `bool` | N | `False` | Use `includedir` instead of `include` |

Example:
```yaml
  - path: /etc/sudoers.d
    is_dir: true
```


## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
