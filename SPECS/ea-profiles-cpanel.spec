Name:           ea-profiles-cpanel
Version:        1.0
Release:        5%{?dist}
Summary:        EasyApache4 Default Profiles
License:        GPL
Group:          System Environment/Configuration
URL:            http://www.cpanel.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package provides the default profiles available from cPanel
to choose from with EasyApache4.

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT/etc/cpanel/ea4/profiles/cpanel
echo -n "Current working dir = "
pwd

install -m 644 ../SOURCES/default.json $RPM_BUILD_ROOT/etc/cpanel/ea4/profiles/cpanel/
install -m 644 ../SOURCES/nophp.json $RPM_BUILD_ROOT/etc/cpanel/ea4/profiles/cpanel/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/etc/cpanel/ea4/profiles/cpanel/default.json
/etc/cpanel/ea4/profiles/cpanel/nophp.json

%changelog
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
