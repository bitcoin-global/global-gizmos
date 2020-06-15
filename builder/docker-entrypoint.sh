#!/bin/bash
set -e

# start required tools
sudo service apt-cacher-ng start

# run whatever
exec "$@"