Name:           gtkgreet
Version:        0.6
Release:        3%{?dist}
Summary:        GTK greeter for greetd
License:        GPL-3.0
URL:            https://git.sr.ht/~kennylevinsen/gtkgreet
Source0:        %{url}/archive/0.6.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  scdoc >= 1.9.7

Requires:       greetd

BuildRequires:  pkgconfig(gtk-layer-shell-0)

%description
A GTK greeter for greetd

%prep
%autosetup

%build
ls -l
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
* Tue Aug 11 2020 Jarkko Oranen <oranenj@iki.fi> - 0.6-2
- rebuilt

* Sat Apr 04 2020 Jarkko Oranen <oranenj@iki.fi> - 0.5-1
- Initial build


