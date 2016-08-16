#!/usr/local/cpanel/3rdparty/bin/perl
# cpanel - pkgs_all_exist.t                       Copyright(c) 2016 cPanel, Inc.
#                                                           All rights Reserved.
# copyright@cpanel.net                                         http://cpanel.net
# This code is subject to the cPanel license. Unauthorized copying is prohibited

use strict;
use warnings;

use Test::More;
use Test::Deep;
use Cpanel::PackMan       ();
use Cpanel::JSON          ();
use Cpanel::Config::Httpd ();
use FindBin;

my @all_profiles;
if ( !Cpanel::Config::Httpd::is_ea4() ) {
    plan skip_all => 'Test irrelevant on non-ea4 machines';
}
else {
    @all_profiles = glob("$FindBin::Bin/../SOURCES/*.json");
    plan tests => @all_profiles * 2;
}

my $pkm = Cpanel::PackMan->instance;
my %ea4_lu;
@ea4_lu{ $pkm->list( prefix => "ea-" ) } = ();

for my $profile (@all_profiles) {
    my $name = ( split( /\//, $profile ) )[-1];
    my $prof_hr = Cpanel::JSON::LoadFile($profile);
    is( ref($prof_hr), 'HASH', "Sanity: have $name hash" );

    cmp_deeply( $prof_hr->{pkgs}, array_each( code( sub { return 1 if exists $ea4_lu{ $_[0] }; return ( 0, "“$_[0]” does not eixst in EA4" ); } ) ), "All $name pkgs exist in ea4" );
}
