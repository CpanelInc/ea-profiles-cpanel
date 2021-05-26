#!/bin/bash

source debian/vars.sh

set -x

perl -pi -e 's/_/-/g' ./*.json
