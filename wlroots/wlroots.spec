# Version of the .so library
%global abi_ver 5
%define git_owner       swaywm
%define git_url         https://github.com/%{git_owner}/%{name}
%define commit          7f9bbaaa17851ba7ee204fc4755ad509e06a9b07
%define abbrev          %(c=%{commit}; echo ${c:0:7})

Name:           wlroots
Version:        0.10.2
Release:        0.git%{abbrev}%{?dist}
Summary:        A modular Wayland compositor library

# Source files/overall project licensed as MIT, but
# - LGPLv2.1+
#   * protocol/idle.xml
#   * protocol/server-decoration.xml
# Those files are processed to C-compilable files by the
# `wayland-scanner` binary during build and don't alter
# the main license of the binaries linking with them by
# the underlying licenses.
License:        MIT
URL:            https://github.com/swaywm/%{name}
Source0:        %{git_url}/archive/%{commit}/%{git_owner}-%{name}-%{abbrev}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.54.0
# FIXME: wlroots require `pkgconfig(egl)`, but assumes mesa provides it
# (and uses it's extension header `<EGL/eglmesaext.h>).
# Upstream is working on not needing that: https://github.com/swaywm/wlroots/issues/1899
# Until it is fixed, pull mesa-libEGL-devel manually
BuildRequires:  pkgconfig(egl) mesa-libEGL-devel
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdrm) >= 2.4.95
BuildRequires:  pkgconfig(libinput) >= 1.9.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(wayland-server) >= 1.18
BuildRequires:  pkgconfig(winpr2)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xkbcommon)

# only select examples are supported for being readily compilable (see SOURCE1)
%global examples \
    cat multi-pointer output-layout pointer rotation screencopy simple tablet touch

%description
%{summary}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}
# not required per se, so not picked up automatically by RPM
Recommends:     pkgconfig(xcb-icccm)
# for examples
Suggests:       gcc
Suggests:       meson >= 0.48.0
Suggests:       pkgconfig(libpng)

%description    devel
Development files for %{name}.


%prep
%setup -q -n %{name}-%{commit}


%build
# Disable options requiring extra/unpackaged dependencies
%{meson} -Dexamples=false -Dlogind-provider=systemd -Dxcb-errors=disabled
%{meson_build}


%install
%{meson_install}

EXAMPLES=( %{examples} )  # Normalize whitespace by creating an array
for example in "${EXAMPLES[@]}"; do
    install -pm0644 -Dt '%{buildroot}/%{_pkgdocdir}/examples' examples/"${example}".[ch]
done


%check
%{meson_test}


%files
%license LICENSE
%doc README.md
%doc %dir %{_pkgdocdir}
%{_libdir}/lib%{name}.so.%{abi_ver}*


%files  devel
%doc %{_pkgdocdir}/examples
%{_includedir}/wlr
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jun 10 2020 Jarkko Oranen <oranenj@iki.fi> - 0.10.2-0
- git master

* Wed Jan 29 2020 Jan Staněk <jstanek@redhat.com> - 0.10.0-2
- Backport fix for compilation with GCC 10

* Tue Jan 28 2020 Joe Walker <grumpey0@gmail.com> - 0.10.0
- Updated to version 0.10.0 (https://github.com/swaywm/wlroots/releases/tag/0.10.0)

Mon Jan 20 2020 Jan Staněk <jstanek@redhat.com> - 0.9.1-1
- Upgrade to version 0.9.1 (https://github.com/swaywm/wlroots/releases/tag/0.9.1)

* Thu Sep 12 2019 Jan Staněk <jstanek@redhat.com> - 0.7.0-2
- Spec file cleanup

* Thu Aug 29 2019 Jeff Peeler <jpeeler@redhat.com> - 0.7.0-1
- Updated to version 0.7.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.6.0-1
- Updated to version 0.6.0
  (see https://github.com/swaywm/wlroots/releases/tag/0.6.0)
- Overhaul dependencies and shipped examples in -devel

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.5.0-2
- Rebuild with Meson fix for #1699099

* Thu Mar 14 2019 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.5.0-1
- Updated to version 0.5.0 (0.2, 0.3, 0.4, 0.4.1 releases effectively skipped)
- Avoid building some parts that are not shipped in binary form, anyway
- Minor spec cleanup (clarify the licensing comment, licensecheck's NTP ~ MIT,
  ldconfig_scriptlets no longer relevant, arch-specific tweak no longer needed)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.1-4
- Fix Firefox crash around text selection/clipboard
  (https://github.com/swaywm/wlroots/pull/1380)

* Tue Nov 27 2018 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.1-3
- Make Firefox run smoother (https://github.com/swaywm/wlroots/pull/1384)

* Wed Nov 07 2018 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.1-2
- Fix incorrect "pkgconfig" version

* Wed Oct 31 2018 Jan Pokorný <jpokorny+rpm-wlroots@fedoraproject.org> - 0.1-1
- Updated to historically first official release
- Turned off implicit enablement of all 'auto' build features under Meson,
  since xcb-errors is not available at this time
- Added BR: libpng
- Expanding spec comment on source files not covered with MIT license

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.9.20180106git03faf17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.8.20180106git03faf17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.7.20180106git03faf17
- Updated snapshot

* Wed Jan 03 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.6.20180102git767df15
- Initial import (#1529352)

* Wed Jan 03 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.5.20180102git767df15
- Updated snapshot

* Sun Dec 31 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.4.20171229git80ed4d4
- Add licensing clarification
- Add BR: gcc

* Sat Dec 30 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.3.20171229git80ed4d4
- Updated snapshot

* Wed Dec 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.2.20171227giteeb7cd8
- Optimize spec-file

* Wed Dec 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.0.1-0.1.20171227giteeb7cd8
- Initial rpm release (#1529352)
