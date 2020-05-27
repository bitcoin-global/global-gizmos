#!/bin/bash
set -e

if [[ "$1" == "bitglob-cli" || "$1" == "bitglob-tx" || "$1" == "bitglobd" || "$1" == "test_bitcoin" ]]; thenn
	exec gosu bitglob "$@"
fi

exec "$@"
