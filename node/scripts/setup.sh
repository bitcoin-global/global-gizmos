#!/bin/sh

################################################################################
#
#                             setup.sh
#
# This is the setup script for Bitcoin node based on Bitcoin Global.
# It takes care of installation of required tools and verification processes
# used across other scripts which are needed for running a Bitcoing Global node.
################################################################################

BLUE='\033[94m'
GREEN='\033[32;1m'
YELLOW='\033[33;1m'
RED='\033[91;1m'
RESET='\033[0m'

print_info() {
    printf "$BLUE$1$RESET\n"
}

print_success() {
    printf "$GREEN$1$RESET\n"
    sleep 1
}

print_warning() {
    printf "$YELLOW$1$RESET\n"
}

print_error() {
    printf "$RED$1$RESET\n"
    sleep 1
}

print_start() {
    print_info "Start date: $(date)"
}

print_end() {
    print_info "\nEnd date: $(date)"
}

# ==================== Configurations