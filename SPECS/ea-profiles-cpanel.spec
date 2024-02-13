Name:           ea-profiles-cpanel

# UGMO: Even though Epoch "is usually omitted because in majority of cases introducing
#       an Epoch value skews the expected RPM behavior when comparing versions of packages."
#       we do it here so that it will work correctly with Cloudlinux’s now-resolved
#       ea-profiles-cpanel issues. See ZC-11574 && "5.3.1. The Epoch directive" at https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/packaging_and_distributing_software/advanced-topics#epoch-scriplets-and-triggers_advanced-topics
#       debs also prefer not using Epoch for similar reasons: https://www.debian.org/doc/debian-policy/ch-controlfields.html#epochs-should-be-used-sparingly
Epoch:          5

Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 69
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        EasyApache4 Default Profiles
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Source1: pkg.postinst
Source2: pkg.prerm
Source3: update-available-profiles

%description
This package provides the default profiles available from cPanel
to choose from with EasyApache4.

%install
rm -rf %{buildroot}
%{__mkdir_p} %{buildroot}/opt/cpanel/ea-profiles-cpanel/bin
%{__mkdir_p} %{buildroot}/etc/cpanel/ea4/profiles/cpanel
install %{SOURCE3} %{buildroot}/opt/cpanel/ea-profiles-cpanel/bin/update-available-profiles

# NOTE: on the distribution of profile files to /etc/cpanel/ea4/profiles/cpanel
#
# Normally a file of the ilk SOURCES/*.json will appear in /opt/cpanel/ea-profiles-cpanel
# UNLESS the file is of the name server-type-XXX-profile_name.json
# server_type is defined by /usr/local/cpanel/server.type, data symlink.
# NOTE: server-type must not contain a dash, so `wp2` is good, whereas `foo-bar` is bad.
#
# This takes advantage of the update-available-profiles that will distribute different profiles based on
# server.type

for file in $(ls %{_sourcedir}/*.json);
do
    base=`basename $file`
    install $file %{buildroot}/opt/cpanel/ea-profiles-cpanel/$base
done

%if 0%{?rhel} > 6
    %if 0%{?rhel} > 8
        rm -f %{buildroot}/opt/cpanel/ea-profiles-cpanel/rubypassenger24.json
        rm -f %{buildroot}/opt/cpanel/ea-profiles-cpanel/rubypassenger27.json
    %else
        rm -f %{buildroot}/opt/cpanel/ea-profiles-cpanel/rubypassenger24.json
        mv -f %{buildroot}/opt/cpanel/ea-profiles-cpanel/rubypassenger27.json %{buildroot}/opt/cpanel/ea-profiles-cpanel/rubypassenger.json
    %endif
%else
    rm -f %{buildroot}/opt/cpanel/ea-profiles-cpanel/rubypassenger27.json
    mv -f %{buildroot}/opt/cpanel/ea-profiles-cpanel/rubypassenger24.json %{buildroot}/opt/cpanel/ea-profiles-cpanel/rubypassenger.json
%endif

%clean
rm -rf %{buildroot}

%posttrans

%include %{SOURCE1}

%preun

%include %{SOURCE2}

%files
%defattr(0644,root,root,0755)
/opt/cpanel/ea-profiles-cpanel
%attr(755,root,root) /opt/cpanel/ea-profiles-cpanel/bin/update-available-profiles

%changelog
* Tue Feb 13 2024 Dan Muey <dan@cpanel.net> - 1.0-69
- ZC-11574: Set epoch to `5` to coordinate w/ Cloudlinux’s fixes

* Wed Jan 03 2024 Brian Mendoza <brian.mendoza@cpanel.net> - 1.0-68
- ZC-11378: Add back original changes, change %post to %posttrans

* Wed Dec 20 2023 Dan Muey <dan@cpanel.net> - 1.0-67
- ZC-11494: Rolling “ea-profiles-cpanel” back to “562229d”: scriptlets seem to be happening out of order on a9

* Fri Dec 15 2023 Brian Mendoza <brian.mendoza@cpanel.net> - 1.0-66
- ZC-11378: Clean up /etc/cpanel/ea4/profiles/cpanel related %files

* Tue Nov 14 2023 Dan Muey <dan@cpanel.net> - 1.0-65
- ZC-11356: Add additional WP2 profiles

* Tue Nov 07 2023 Julian Brown <julian.brown@cpanel.net> - 1.0-64
- ZC-11352: Allow WP2 to provide a directory of profiles as the default

* Fri Oct 06 2023 Brian Mendoza <brian.mendoza@cpanel.net> - 1.0-63
- ZC-11253: Update EA4 profiles - Add ea-php82, Remove ea-php80

* Thu Jun 15 2023 Dan Muey <dan@cpanel.net> - 1.0-62
- ZC-10971: Add WP² profile and license-based profile support

* Fri Mar 31 2023 Thomas Baugh <thomas.baugh@cpanel.net> - 1.0-61
- Don't ship rubypassenger27.json on CentOS 9+

* Tue Jan 10 2023 Dan Muey <dan@cpanel.net> - 1.0-60
- ZC-10584: Drop special C7 allphp profiles since PHP 8.2 is available on C7

* Thu Dec 22 2022 Dan Muey <dan@cpanel.net> - 1.0-59
- ZC-10447: Update profiles for PHP 7.4 being EOL and PHP 8.2 being available

* Wed Mar 16 2022 Julian Brown <julian.brown@cpanel.net> - 1.0-58
- ZC-9823: Update profiles for PHP8

* Wed Jan 12 2022 Dan Muey <dan@cpanel.net> - 1.0-57
- ZC-8539: Create Default NGINX® profile

* Wed Dec 08 2021 Julian Brown <julian.brown@cpanel.net> - 1.0-56
- ZC-9367: Add php-zip to default profile

* Mon Dec 06 2021 Travis Holloway <t.holloway@cpanel.net> - 1.0-55
- EA-10325: Update “mpm_itk worker” profile(s):  add “ea-php74”
- EA-10325: Update “allphp allphp-opcache default mpm_itk worker” profile(s):  remove “ea-php73”

* Mon Nov 08 2021 Dan Muey <dan@cpanel.net> - 1.0-54
- ZC-9469: remove ea-php..-build from allphp-opcache.json

* Fri Mar 12 2021 Cory McIntire <cory@cpanel.net> - 1.0-53
- EA-9481: Update Phusion passenger version

* Tue Mar 02 2021 Travis Holloway <t.holloway@cpanel.net> - 1.0-52
- EA-9613: Update “allphp allphp-opcache default” profile(s):  add “ea-php80” based on “ea-php73”

* Thu Dec 10 2020 Daniel Muey <dan@cpanel.net> - 1.0-51
- ZC-7620: Update Ruby profile for 2.7 on C7 and C8

* Mon Dec 07 2020 Cory McIntire <cory@cpanel.net> - 1.0-50
- EA-9444: Remove ea-php72 from all profiles

* Mon Oct 05 2020 Daniel Muey <dan@cpanel.net> - 1.0-49
- ZC-7499: Update “default” profile:  add “ea-php74” based on “ea-php73”

* Thu Jul 23 2020 Tim Mullin <tim@cpanel.net> - 1.0-48
- EA-9154: Add iconv and mbstring to the mpm_itk and worker profiles

* Thu May 07 2020 Tim Mullin <tim@cpanel.net> - 1.0-47
- EA-9045: Remove PHP 7.1 from the profiles since it is EOL

* Wed Apr 15 2020 Julian Brown <julian.brown@cpanel.net> - 1.0-46
- ZC-6297: Add PHP 7.4 to all and all opcache
- ZC-6283: order allphp* tags lowest to highest like the rest

* Fri Mar 06 2020 Cory McIntire <cory@cpanel.net> - 1.0.45
- EA-8905: Revert PHP 7.4 from profiles as it was breaking smokers.

* Tue Feb 18 2020 Daniel Muey <dan@cpanel.net> - 1.0-44
- ZC-5923: Add PHP 7.4 where appropriate

* Mon Feb 17 2020 Tim Mullin <tim@cpanel.net> - 1.0-43
- EA-8864: Add php73 to the mpm_itk and worker profiles

* Thu Dec 12 2019 Travis Holloway <t.holloway@cpanel.net> - 1.0-42
- ZC-5770: Add iconv and mbstring to the default profile

* Thu Jun 06 2019 Daniel Muey <dan@cpanel.net> - 1.0-41
- ZC-4757: Add PHP 7.3 to the default profile

* Thu Apr 25 2019 Daniel Muey <dan@cpanel.net> - 1.0-40
- ZC-4685: Add ea-nodejs10 to passenger profile

* Mon Feb 11 2019 Daniel Muey <dan@cpanel.net> - 1.0-39
- ZC-4701: Add PHP 7.3 to the all-PHP profiles

* Tue Jan 29 2019 Daniel Muey <dan@cpanel.net> - 1.0-38
- ZC-4736: Add 7.2 to PHP profiles that should have it

* Thu Jan 24 2019 Justin Schaefer <justins@cpanel.net> - 1.0-37
- EA-4717 Remove PHP 5.6 and 7.0 from default EasyApache profiles

* Wed Jan 09 2019 Daniel Muey <dan@cpanel.net> - 1.0-36
- remove lsapi profile until the yum repo problem on CL boxes can be addressed

* Wed Jan 02 2019 Tim Mullin <tim@cpanel.net> - 1.0-35
- EA-8110: Correct description for the "cPanel Default + MPM ITK" profile

* Wed Nov 28 2018 Daniel Muey <dan@cpanel.net> - 1.0-34
- ZC-4444: Add lsapi profile

* Tue Jun 05 2018 Cory McIntire <cory@cpanel.net> - 1.0-33
- EA-7541: remove ea-php55-php-fpm and duplicated ea-php56/70-php-fpm

* Mon May 07 2018 Cory McIntire <cory@cpanel.net> - 1.0-32
- EA-7447: Add 7.2 to All PHPs and All PHPs opcache profiles

* Tue Apr 17 2018 Daniel Muey <dan@cpanel.net> - 1.0-31
- EA-7172: Remove EOL PHPs from profiles, add 7.1

* Thu Jun 08 2017 Rishwanth Yeddula <rish@cpanel.net> - 1.0-30
- Update the "Ruby via Passenger" profile to include additional Ruby gems

* Sun May 21 2017 Rishwanth Yeddula <rish@cpanel.net> - 1.0-29
- Added a basic "Ruby via Passenger" profile

* Tue Apr 25 2017 Jacob Perkins <jacob.perkins@cpanel.net> - 1.0-28
- Added PHP70 opcache to allphp-opcache profile

* Fri Dec 16 2016 Jacob Perkins <jacob.perkins@cpanel.net> - 1.0-27
- EA-5493: Added vendor field

* Tue Aug 16 2016 Dan Muey <dan@cpanel.net> - 1.0-26
- EA-5025: remove packages from profiles that do not exist

* Mon Jun 20 2016 Dan Muey <dan@cpanel.net> - 1.0-25
- EA-4383: Update Release value to OBS-proof versioning

* Mon Jun 20 2016 Sricharan Angara <charan@cpanel.net> - 1.0-15
- Removed duplicate PHP FPM packages for PHP 5.5, PHP 5.6 and PHP 7.0 respectively from allphp.json and allphp-opcache.json profiles. (ZC-1956)

* Thu Jun 02 2016 S. Kurt Newman <kurt.newman@cpanel.net> - 1.0-14
- Added mod_security2 apache module to default and itk profiles (EA-4655)
- Spec file cleanup (EA-4655)

* Mon May 23 2016 Jacob Perkins <jacob.perkins@cpanel.net> - 1.0-13
- Fixed previous changelog entry

* Tue May 17 2016 Darren Mobley <darren@cpanel.net> - 1.0-12
- Removed PHP 5.4 from profiles with PHP
- Adding PHP 7.0 to profiles with PHP
- Added PHP-FPM to all profiles that have PHP
- Moved the previous default profile to a "worker" profile
- Created a new default profile from the old ruid2 profile that uses mpm_prefork, ruid2

* Tue Nov 10 2015 Dan Muey <dan@cpanel.net> - 1.0-11
- ensure no profiles have 2 or more DSO PHP RPMs

* Wed Oct 28 2015 Julian Brown <julian.brown@cpanel.net> - 1.0-10
- Add php-xml to all php profiles

* Tue Aug 11 2015 Trinity Quirk <trinity.quirk@cpanel.net> - 1.0-9
- Updated all profiles to approximately match those provided by EA3
- Added new mcrypt extension to all profiles

* Wed Aug 05 2015 Dan Muey <dan@cpanel.net> - 1.0-8
- ensure some basics in all profiles

* Tue Aug 04 2015 Dan Muey <dan@cpanel.net> = 1.0-7
- use prefork mpm for ruid2

* Mon Aug 03 2015 Dan Muey <dan@cpanel.net> - 1.0-6
- Add allphp, mpm_itk, and ruid2 profiles.
- simplify files rpm section

* Mon Aug 03 2015 Julian Brown <julian.brown@cpanel.net> - 1.0-5
- Added ea-apache24-mod-cgid to nophp profile.

* Fri Jun 05 2015 Darren Mobley <darren@cpanel.net> - 1.0-4
- Removed ea-httpd package from profiles

* Wed Jun 03 2015 Darren Mobley <darren@cpanel.net> - 1.0-3
- Bumped version for addition of mysql for php support

* Wed May 27 2015 Darren Mobley <darren@cpanel.net> - 1.0-2
- Updated profiles to reflect change from ea-apache2 to ea-apache24

* Tue May 26 2015 Darren Mobley <darren@cpanel.net> - 1.0-1
- Initial Profiles RPM creation
