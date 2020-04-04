Name:           greetd
Summary:        A login manager daemon
License:        GPL-3.0-or-later
Version:        0.5.1
Release:        1%{?dist}
URL:            https://git.sr.ht/~kennylevinsen/greetd

Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  scdoc

%description
A login manager daemon

%global debug_package %{nil}

%prep
%autosetup

%build
cargo build --release
scdoc < man/agreety-1.scd | gzip -9 > man/agreety.1.gz
scdoc < man/greetd-1.scd | gzip -9 > man/greetd.1.gz
scdoc < man/greetd-ipc-7.scd | gzip -9 > man/greetd-ipc.7.gz
scdoc < man/greetd-5.scd | gzip -9 > man/greetd.5.gz

%install
install -D -m755 target/release/%{name} %{buildroot}/%{_bindir}/%{name}
install -D -m755 target/release/agreety %{buildroot}/%{_bindir}/agreety
install -D -m0644 greetd.service %{buildroot}/%{_unitdir}/greetd.service
install -D -m0644 config.toml %{buildroot}/etc/greetd/config.toml
install -D -m0644 man/greetd.1.gz %{buildroot}/%{_mandir}/man1/agreety.1.gz
install -D -m0644 man/greetd.1.gz %{buildroot}/%{_mandir}/man1/greetd.1.gz
install -D -m0644 man/greetd.5.gz %{buildroot}/%{_mandir}/man5/greetd.5.gz
install -D -m0644 man/greetd-ipc.7.gz %{buildroot}/%{_mandir}/man7/greetd.7.gz

%files
%{_bindir}/greetd
%{_bindir}/agreety
%{_unitdir}/greetd.service
%{_mandir}/*
%config /etc/greetd/config.toml

%pre
getent group greetd >/dev/null || groupadd -r greetd
getent passwd greetd >/dev/null || \
    useradd -r -g greetd -d /etc/greetd -s /sbin/nologin \
    -c "Login manager daemon" greetd
exit 0

%changelog
* Fri Apr 02 2020 Jarkko Oranen <oranenj@iki.fi> 0.5.1-1
- Initial build

