Summary:	Profile based systemd network management
Name:		netctl
Version:	1.2
Release:	3
License:	GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Base
Source0:	https://projects.archlinux.org/netctl.git/snapshot/%{name}-%{version}.tar.gz
# Source0-md5:	697f5c1a386d04506784dda4a8b1a781
BuildRequires:	asciidoc
Requires:	coreutils
Requires:	iproute2
Requires:	resolvconf
Requires:	systemd
Suggests:	dhcpcd
Suggests:	dialog
Suggests:	wpa_supplicant
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
netctl may be used to introspect and control the state of the systemd
services for the network profile manager.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D contrib/zsh-completion \
	$RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_netctl

%{__rm} -r $RPM_BUILD_ROOT%{_sysconfdir}/netctl/examples

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README docs/examples/*
%attr(755,root,root) %{_bindir}/netctl
%attr(755,root,root) %{_bindir}/netctl-auto
%attr(755,root,root) %{_bindir}/wifi-menu

%dir %{_sysconfdir}/netctl
%dir %{_sysconfdir}/netctl/hooks

%dir %{_prefix}/lib/network
%dir %{_prefix}/lib/network/connections
%attr(755,root,root) %{_prefix}/lib/network/auto.action
%attr(755,root,root) %{_prefix}/lib/network/network
%{_prefix}/lib/network/connections/bond
%{_prefix}/lib/network/connections/bridge
%{_prefix}/lib/network/connections/ethernet
%{_prefix}/lib/network/connections/mobile_ppp
%{_prefix}/lib/network/connections/pppoe
%{_prefix}/lib/network/connections/tunnel
%{_prefix}/lib/network/connections/tuntap
%{_prefix}/lib/network/connections/vlan
%{_prefix}/lib/network/connections/wireless
%{_prefix}/lib/network/globals
%{_prefix}/lib/network/ip
%{_prefix}/lib/network/rfkill
%{_prefix}/lib/network/wpa

%{systemdunitdir}/netctl@.service
%{systemdunitdir}/netctl.service
%{systemdunitdir}/netctl-sleep.service
%{systemdunitdir}/netctl-auto@.service

%{_mandir}/man1/netctl.1*
%{_mandir}/man5/netctl.profile.5*
%{_mandir}/man7/netctl.special.7*

%{_datadir}/zsh/site-functions/_netctl

%if 0
/etc/ifplugd/netctl.action
%{systemdunitdir}/netctl-ifplugd@.service
%endif

