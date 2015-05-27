Name:           ea-profiles-cpanel
Version:        1.0
Release:        1%{?dist}
Summary:        EasyApache4 Default Profiles
License:        GPL
Group:          System Environment/Configuration
URL:            http://www.cpanel.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:       ea-apache2-config

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
* Thu May 25 2015 Darren Mobley <darren@cpanel.net> - 1.0-1
- Initial Profiles RPM creation
