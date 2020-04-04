Name:           gtkgreet
Version:        0.5
Release:        1%{?dist}
Summary:        GTK greeter for greetd
License:        GPL-3.0
URL:            https://git.sr.ht/~kennylevinsen/gtkgreet
Source0:        %{url}/archive/0.5.tar.gz
Patch0:         fix-link-failure.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  scdoc >= 1.9.7

Requires:       greetd

BuildRequires:  pkgconfig(gtk-layer-shell-0)

%description
A GTK greeter for greetd

%prep
%autosetup -p1

%build
%meson -Dlayershell=true
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_mandir}/man1/*
%{_bindir}/gtkgreet

%changelog
* Sat Apr 04 2020 Jarkko Oranen <oranenj@iki.fi> - 0.5-1
- Initial build


