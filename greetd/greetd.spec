Name:           greetd
Summary:        A login manager daemon
License:        GPL-3.0-or-later
Version:        0.5.1
Release:        2%{?dist}
URL:            https://git.sr.ht/~kennylevinsen/greetd

Source0:        %{url}/archive/%{version}.tar.gz
Source1:        sway-config

BuildRequires:  cargo
BuildRequires:  scdoc

Requires: pam
Requires: audit-libs
Requires: systemd
Requires(post): policycoreutils
Requires(postun): policycoreutils

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
mkdir -p %{buildroot}/run/greetd
install -D -m0755 target/release/%{name} %{buildroot}/%{_sbindir}/%{name}
install -D -m0755 target/release/agreety %{buildroot}/%{_bindir}/agreety
sed -i 's#ExecStart.*#ExecStart=greetd -s /run/greetd/greetd.sock#g' greetd.service
install -D -m0644 greetd.service %{buildroot}/%{_unitdir}/greetd.service

sed -i 's/"greeter"/"greetd"/g' config.toml
install -D -m0644 config.toml %{buildroot}/etc/greetd/config.toml
install -D -m0644 %{SOURCE1} %{buildroot}/etc/greetd/sway-config


install -D -m0644 man/greetd.1.gz %{buildroot}/%{_mandir}/man1/agreety.1.gz
install -D -m0644 man/greetd.1.gz %{buildroot}/%{_mandir}/man1/greetd.1.gz
install -D -m0644 man/greetd.5.gz %{buildroot}/%{_mandir}/man5/greetd.5.gz
install -D -m0644 man/greetd-ipc.7.gz %{buildroot}/%{_mandir}/man7/greetd.7.gz

%files
%{_sbindir}/greetd
%{_bindir}/agreety
%{_unitdir}/greetd.service
%{_mandir}/*
%config /etc/greetd/config.toml
%config /etc/greetd/sway-config
%attr(0775, greetd, greetd) %dir /run/greetd

%pre
getent group greetd >/dev/null || groupadd -r greetd
getent passwd greetd >/dev/null || \
    useradd -r -g greetd -G video -d /etc/greetd -s /sbin/nologin \
    -c "Login manager daemon" greetd
exit 0


%post
semanage fcontext -a -t xdm_exec_t %{_sbindir}/%{name} 2>/dev/null || :
semanage fcontext -a -t xdm_var_run_t '/var/run/greetd(/.*)?' 2>/dev/null || :
restorecon -R '/run/greetd' '%{_sbindir}/%{name}' || :
%systemd_post greetd.service

%preun
%systemd_preun greetd.service

%postun 
if [ $1 -eq 0 ] ; then  # final removal
semanage fcontext -d -t xdm_exec_t '%{_bindir}/%{name}' 2>/dev/null || :
semanage fcontext -d -t xdm_var_run_t '/var/run/greetd(/.*)?' 2>/dev/null || :
fi
%systemd_postun greetd.service

%changelog
* Sat Apr 04 2020 Jarkko Oranen <oranenj@iki.fi> - 0.5.1-2
- SELinux support and sway config

* Fri Apr 03 2020 Jarkko Oranen <oranenj@iki.fi> 0.5.1-1
- Initial build

