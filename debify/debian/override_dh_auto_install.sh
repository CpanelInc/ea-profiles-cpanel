#!/bin/bash

source debian/vars.sh

rm -rf $buildroot
mkdir -p $buildroot/etc/cpanel/ea4/profiles/cpanel
install $_sourcedir/*.json $buildroot/etc/cpanel/ea4/profiles/cpanel/
rm -f $buildroot/etc/cpanel/ea4/profiles/cpanel/rubypassenger24.json
mv -f $buildroot/etc/cpanel/ea4/profiles/cpanel/rubypassenger27.json $buildroot/etc/cpanel/ea4/profiles/cpanel/rubypassenger.json
