%if 0%{?rhel} >= 8 || 0%{?fedora} >= 19
%bcond_without python3
%else
%bcond_with python3
%endif

%define commit a2177ed9942477868ccc514372f32a0fbcbe189e

Name:    redshift
Version: 1.12.gita2177ed
Release: 2%{dist}
Summary: Adjusts the color temperature of your screen according to time of day
License: GPLv3+

URL:     http://jonls.dk/redshift/
Source0: https://github.com/minus7/redshift/archive/wayland.tar.gz

BuildRequires: libtool
BuildRequires: intltool
BuildRequires: gettext-devel
BuildRequires: libdrm-devel
BuildRequires: libXrandr-devel
BuildRequires: libXxf86vm-devel
BuildRequires: GConf2-devel
BuildRequires: geoclue2-devel
BuildRequires: wayland
BuildRequires: wayland-protocols
%{?systemd_requires}
BuildRequires: systemd

%description
Redshift adjusts the color temperature of your screen according to your
surroundings. This may help your eyes hurt less if you are working in
front of the screen at night.

The color temperature is set according to the position of the sun. A
different color temperature is set during night and daytime. During
twilight and early morning, the color temperature transitions smoothly
from night to daytime temperature to allow your eyes to slowly
adapt.

This package provides the base program.

%package -n %{name}-gtk
Summary:       GTK integration for Redshift

BuildRequires: desktop-file-utils
%if %{with python3}
BuildRequires: python3-devel >= 3.2
Requires:      python3-gobject
Requires:      python3-pyxdg
%else
BuildRequires: python2-devel
Requires:      pygobject3
Requires:      pyxdg
%endif
Requires:      %{name} = %{version}-%{release}
Obsoletes:      gtk-%{name} < 1.7-7

%description -n %{name}-gtk
This package provides GTK integration for Redshift, a screen color
temperature adjustment program.

%prep
%autosetup -N -n %{name}-%{commit}
%if %{without python3}
%patch0 -p1
%endif
autopoint -f && AUTOPOINT="intltoolize --automake --copy" autoreconf -f -i

%build
%configure --with-systemduserunitdir=%{_userunitdir}
%make_build V=1

%install
%make_install
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/redshift.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/redshift-gtk.desktop

%post
%systemd_user_post %{name}-gtk.service

%preun
%systemd_user_preun %{name}-gtk.service


%files -f %{name}.lang
%doc DESIGN CONTRIBUTING.md NEWS NEWS.md README README-colorramp README.md redshift.conf.sample
%license COPYING
%{_bindir}/redshift
%{_mandir}/man1/*
%{_datadir}/applications/redshift.desktop
%{_userunitdir}/%{name}.service

%files -n %{name}-gtk
%{_bindir}/redshift-gtk
%if %{with python3}
%{python3_sitelib}/redshift_gtk/
%else
%{python2_sitelib}/redshift_gtk/
%endif
%{_datadir}/icons/hicolor/scalable/apps/redshift*.svg
%{_datadir}/applications/redshift-gtk.desktop
%{_datadir}/appdata/redshift-gtk.appdata.xml
%{_userunitdir}/%{name}-gtk.service

%changelog
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.12-1
- Update to 1.12 (#1581005)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.11-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Milos Komarcevic <kmilos@gmail.com> - 1.11-1
- Update to 1.11 (#1295151)

* Mon Dec 07 2015 Milos Komarcevic <kmilos@gmail.com> - 1.10-6
- Fix broken doc symlinks (#1222341)

* Mon Dec 07 2015 Matěj Cepl <mcepl@redhat.com> - 1.10-5
- Make buildable on EPEL (#1204257)

* Sun Nov 22 2015 Milos Komarcevic <kmilos@gmail.com> - 1.10-4
- Add a redshift desktop file (#1214978)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 07 2015 Milos Komarcevic <kmilos@gmail.com> - 1.10-1
- Update to 1.10 (#1178819)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 23 2014 Milos Komarcevic <kmilos@gmail.com> - 1.9.1-1
- Update to 1.9.1 (#1090018)

* Sat Nov 30 2013 Milos Komarcevic <kmilos@gmail.com> - 1.8-1
- Update to 1.8 (#1029155)
- Source comes from GitHub now

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Milos Komarcevic <kmilos@gmail.com> - 1.7-5
- Run autoreconf to support aarch64 (#926436)
- Backport fix for geoclue client check (#954014)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 9 2011 Milos Komarcevic <kmilos@gmail.com> - 1.7-1
- Update to 1.7
- Add geoclue BuildRequires
- Change default geoclue provider from Ubuntu GeoIP to Hostip
- Remove manual Ubuntu icons uninstall

* Mon Feb 28 2011 Milos Komarcevic <kmilos@gmail.com> - 1.6-3
- Fix for clock applet detection (#661145)
- Require pyxdg explicitly (#675804)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 13 2010 Milos Komarcevic <kmilos@gmail.com> - 1.6-1
- Update to 1.6
- Remove BuildRoot tag and clean section

* Thu Aug 26 2010 Milos Komarcevic <kmilos@gmail.com> - 1.5-1
- Update to 1.5
- Install desktop file

* Mon Jul 26 2010 Milos Komarcevic <kmilos@gmail.com> - 1.4.1-2
- License updated to GPLv3+
- Added python macros to enable building on F12 and EPEL5
- Specific python version BR
- Subpackage requires full base package version
- Increased build log verbosity
- Preserve timestamps on install

* Thu Jun 17 2010 Milos Komarcevic <kmilos@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Thu Jun 10 2010 Milos Komarcevic <kmilos@gmail.com> - 1.3-1
- Initial packaging
