%define release_prefix 15

Name:           ea-profiles-cpanel
Version:        1.0
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        EasyApache4 Default Profiles
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
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
