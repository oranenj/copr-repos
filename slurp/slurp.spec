Name:           slurp
Version:        1.3.0
Release:        1%{?dist}
Summary:        Wayland tool for selecting screen regions

License:        MIT
URL:            https://github.com/emersion/slurp
Source0:        https://github.com/emersion/slurp/releases/download/v%{version}/slurp-%{version}.tar.gz

BuildRequires:  gcc, meson, cairo-devel, wayland-devel, pkgconfig(wayland-protocols), scdoc

%description
Select a screen region and output its geometry; useful in conjunction with grim.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
/usr/bin/slurp
/usr/share/man/man1/slurp.1.gz

%changelog
* Tue Nov 19 2019 Jarkko Oranen
- 1.2.0

