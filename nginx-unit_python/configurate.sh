#!/bin/bash
docker exec -it $1 curl -X PUT -d @/config/config.json --unix-socket \
/var/run/control.unit.sock http://localhost/config
