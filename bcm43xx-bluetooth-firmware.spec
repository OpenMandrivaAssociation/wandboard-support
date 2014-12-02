Name:		bcm43xx-bluetooth-firmware
Version:	1.0
Release:	1
Summary:	Firmware & loader for Broadcom bcm43xx Bluetooth chipsets
Group:		System/Kernel and hardware
License:	Proprietary
URL:		http://www.wandboard.org
Source0:	%{name}-%{version}.tar.xz
Requires:	bluez
ExclusiveArch:	%{armx}

%description
Firmware & loader for Broadcom bcm4329 & bcm4330 Bluetooth chipsets.

%prep
%setup -q

%build
%{__cc} %{optflags} %{ldflags} -o brcm_patchram_plus brcm_patchram_plus.c

%install
install -m755 brcm_patchram_plus -D %{buildroot}%{_sbindir}/brcm_patchram_plus
install -p -m755 bcm43xx-firmware-load %{buildroot}%{_sbindir}/bcm43xx-firmware-load
install -p -m644 bcm4329.hcd -D %{buildroot}/lib/firmware/brcm/bcm4329.hcd
install -p -m644 bcm4330.hcd -D %{buildroot}/lib/firmware/brcm/bcm4330.hcd
install -p -m644 bcm43xx.sysconfig -D %{buildroot}%{_sysconfdir}/sysconfig/bcm43xx
install -p -m644 bcm43xx-bluetooth.service -D %{buildroot}%{_unitdir}/bcm43xx-bluetooth.service
install -d %{buildroot}%{_presetdir}
tee > %{buildroot}%{_presetdir}/10-bcm43xx-bluetooth.preset <<EOF
enable bcm43xx-bluetooth.service
EOF

%files
%{_sbindir}/brcm_patchram_plus
%{_sbindir}/bcm43xx-firmware-load
%config(noreplace) %{_sysconfdir}/sysconfig/bcm43xx
/lib/firmware/brcm/bcm4329.hcd
/lib/firmware/brcm/bcm4330.hcd
%{_unitdir}/bcm43xx-bluetooth.service
%{_presetdir}/10-bcm43xx-bluetooth.preset

%changelog
* Tue Dec  2 2014 Per Øyvind Karlsen <peroyvind@moondrake.org> 1.0-1
- initial mdk release
