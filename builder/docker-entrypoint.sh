#!/bin/bash
set -e

# start required tools
dockerd &> /dev/null &
/etc/init.d/apt-cacher-ng start &> /dev/null

# run whatever
exec "$@"