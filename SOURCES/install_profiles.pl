#!/usr/bin/env perl

use strict;
use warnings;

my $sourcedir = $ARGV[0];
my $buildroot = $ARGV[1];

my @source = split( /\n/, `find $sourcedir -name "*.json" -print` );
foreach my $file (@source) {
    my $basename = substr( $file, length($sourcedir) + 1 );
    print "File :$file: :$basename:\n";

    # NOTE: server-type must not contain a dash, so `wp2` is good, whereas `foo-bar` is bad.
    if ( $basename =~ m/^(server-type-[^-]+)-(.+)$/ ) {
        my $server_type = $1;
        my $filename    = $2;

        my $target_dir = "$buildroot/opt/cpanel/ea-profiles-cpanel/$server_type";
        system( 'mkdir',   '-p',   $target_dir );
        system( 'chmod',   '0755', $target_dir );
        system( 'install', $file,  "$target_dir/$filename" );
    }
    else {
        my $target_dir = "$buildroot/opt/cpanel/ea-profiles-cpanel";
        system( 'install', $file, "$target_dir/$basename" );
    }
}

