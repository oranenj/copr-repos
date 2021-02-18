%define git_owner       oranenj
%define git_url         https://github.com/%{git_owner}/%{name}
%define commit          4ecb1aa27e71d8609fb073e8c4bc3945fccd71ef
%define abbrev          %(c=%{commit}; echo ${c:0:7})
Name:           xdg-desktop-portal-wlr
Summary:        xdg-desktop-portal backend for wlroots
License:        MIT
Release:        1
URL:            %{git_url}

Version:        0.2.1
Source0:        %{git_url}/archive/%{commit}/%{git_owner}-%{name}-%{abbrev}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.2.9
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  iniparser-devel


%description
xdg-desktop-portal backend for wlroots

%prep
%autosetup -N -n %{name}-%{commit}


%build
%meson -Dsd-bus-provider=libsystemd
%meson_build


%install
%meson_install


%files
/usr/libexec/xdg-desktop-portal-wlr
/usr/share/xdg-desktop-portal/portals/wlr.portal
/usr/lib/systemd/user/xdg-desktop-portal-wlr.service
/usr/share/dbus-1/services/org.freedesktop.impl.portal.desktop.wlr.service


%changelog
* Thu Oct 29 2020 Jarkko Oranen <oranenj@iki.fi> - 0.2.0-1
- Output chooser support

* Thu May 21 2020 Jarkko Oranen <oranenj@iki.fi> - 0.1.0-1
- Upstream released 0.1.0

* Sat Feb 01 2020 Jarkko Oranen
- Initial version
