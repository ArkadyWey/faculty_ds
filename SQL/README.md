# SQL

Install and set up postgresql on the current server
by running `setup-postgresql.sh`:

```bash
./setup-postgresql.sh
```

Then go through the notebooks.

### For instructors

Be aware of `.img` and `.queries`
(not displayed in the Workspace UI by default).
Careful when editing `setup-postgresql.sh` in
the basic Platform editor: it will reset its
permissions on save (use code-server or vim to
edit if you have to). To restore the permissions:

```bash
chmod 777 setup-postgresql.sh
```

