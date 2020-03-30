%define git_owner       emersion
%define git_url         https://github.com/%{git_owner}/%{name}
%define commit          dfa0ac704064304824b6d4fea7870d33359dcd15
%define abbrev          %(c=%{commit}; echo ${c:0:7})
Name:           xdg-desktop-portal-wlr
Summary:        xdg-desktop-portal backend for wlroots
License:        MIT
Release:        1%{?dist}
URL:            %{git_url}

Version:        0.0
Source0:        %{git_url}/archive/%{commit}/%{git_owner}-%{name}-%{abbrev}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.2.9
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14


%description
xdg-desktop-portal backend for wlroots

%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
/usr/bin/xdg-desktop-portal-wlr
/usr/share/xdg-desktop-portal/portals/wlr.portal

%changelog
* Sat Feb 01 2020 Jarkko Oranen
- Initial version
