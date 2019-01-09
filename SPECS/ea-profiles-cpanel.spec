Name:           ea-profiles-cpanel
Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 36
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        EasyApache4 Default Profiles
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package provides the default profiles available from cPanel
to choose from with EasyApache4.

%install
rm -rf %{buildroot}
%{__mkdir_p} %{buildroot}/etc/cpanel/ea4/profiles/cpanel
install %{_sourcedir}/*.json %{buildroot}/etc/cpanel/ea4/profiles/cpanel/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
/etc/cpanel/ea4/profiles/cpanel

%changelog
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

* Tue May 15 2016 Darren Mobley <darren@cpanel.net> - 1.0-12
- Removed PHP 5.4 from profiles with PHP
- Adding PHP 7.0 to profiles with PHP
- Added PHP-FPM to all profiles that have PHP
- Moved the previous default profile to a "worker" profile
- Created a new default profile from the old ruid2 profile that uses mpm_prefork, ruid2

* Mon Nov 10 2015 Dan Muey <dan@cpanel.net> - 1.0-11
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
