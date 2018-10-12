# Ansible Role SSL

This role creates and manages an arbitrary, variable-ized set of SSL-related
directories and files.

### To-dos

- Add self-signed SSL generation.

## Role Variables

| Variable name     | Default value | Description |
|-------------------|---------------|-------------|
| `ssl_directories` | `[]`          | A list of remote directories to create or configure. Supports the `path`, `owner`, `group`, and `mode` parameters from the Ansible File module. |
| `ssl_files`       | `[]`          | A list of SSL keys and certificates to copy to the remote server. Supports the `src`, `dest`, `owner`, `group`, and `mode` parameters from the Ansible Copy module. |

## Example Playbook

The following playbook creates/configures:

  - `/etc/ssl/certs`
  - `/etc/ssl/private`
  - `/etc/ssl/certs/www.example.com.crt`
  - `/etc/ssl/private/www.example.com.key`

    - hosts: all
      vars:
        ssl_directories:
          - path: "/etc/ssl/certs"
            owner: root
            group: root
            mode: "u=rwx,go=rx"
          - path: "/etc/ssl/private"
            owner: root
            group: root
            mode: "u=rwx,go=rx"
        ssl_files:
          - src: "{{ playbook_dir }}/certs/www.example.com.crt"
            dest: "/etc/ssl/certs/www.example.com.crt"
            owner: root
            group: root
            mode: "u=rw,go=r"
          - src: "{{ playbook_dir }}/certs/www.example.com.key"
            dest: "/etc/ssl/private/www.example.com.key"
            owner: root
            group: root
            mode: "u=rw,go="
      roles:
        - role: ansible-role-ssl

## License

GPLv3
