#!/bin/bash

source debian/vars.sh

set -x

# ZC-9464: ideally this would happen automatically by virtue of
#   remove_from_install/remove_from_specific_install when its
#   making the tarball of SOURCES (need_to_generate_source_tarball is true)
rm -rf rubypassenger27.json
rm -rf allphp-c7*.json

perl -pi -e 's/_/-/g' ./*.json
