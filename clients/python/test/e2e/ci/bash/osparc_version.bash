#!/bin/bash

set -o errexit  # abort on nonzero exitstatus
set -o nounset  # abort on unbound variable
set -o pipefail # don't hide errors within pipes

version=$1
report=$(mktemp)
trap 'rm -rf ${report}' ERR

if [ "${version}" == "latest_release" ]; then
    pip install osparc --dry-run --quiet --report "${report}"
elif [ "${version}" == "latest_master" ]; then
    pip install osparc --dry-run --quiet --pre --report "${report}"
else
    pip install osparc=="${version}" --dry-run --quiet --report "${report}"
fi
jq -r '.install[] | select(.metadata.name == "osparc") | .metadata.version' "${report}"
rm -rf "${report}"
