%define	major	4
%define	libname	%mklibname vpu %{major}
%define	devname	%mklibname -d vpu

Summary:	Firmware & tools for Wandboard support
Name:		wandboard-support
Version:	1.0
Release:	3
License:	Proprietary ASL 2.0 GPLv3
Group:		System/Kernel and hardware
URL:		https://abf.io/software/wandboard-support
Source0:	%{name}-%{version}.tar.xz
Requires:	%{name}-bcm43xx-bluetooth-firmware = %{EVRD}
Requires:	%{name}-bcm43xx-wifi-firmware = %{EVRD}
Requires:	%{name}-vpu-firmware = %{EVRD}
ExclusiveArch:	armv7hl armv7hnl

%description
This package contains scripts and firmware to support the Wandboard.

%package	bcm43xx-bluetooth-firmware
Summary:	Firmware for BCM4329 & BCM4330 Bluetooth chips
Group:		System/Kernel and hardware
Requires:	bluez
%rename		bcm43xx-bluetooth-firmware

%description	bcm43xx-bluetooth-firmware
This package contains firmware for the Broadcom BCM4329 & BCM4330 Bluetooth
chips, together with their loader tool.

%package	bcm43xx-wifi-firmware
Summary:	Firmware for BCM4329 & BCM4330 WiFi chips
Group:		System/Kernel and hardware

%description	bcm43xx-wifi-firmware
This package contains firmware for the Broadcom BCM4329 & BCM4330 WiFi chips.

%package	vpu-firmware
Summary:	Firmware IMX6D & IMX6Q VPU
Group:		System/Kernel and hardware

%description	vpu-firmware
This package contains firmware for the IMX6D & IMX6Q Video Processing Unit.

%package	mkbootlogo
Summary:	Tool for creating boot splash
Group:		System/Configuration/Boot and Init
Requires:	imagemagick

%description	mkbootlogo
This package contains a simple script to create HDMI bootlogos an utility to
reduce artifacts in them.

%prep
%setup -q

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall_std

%files

%files bcm43xx-bluetooth-firmware
%{_sbindir}/brcm_patchram_plus
%{_sbindir}/bcm43xx-firmware-load
%config(noreplace) %{_sysconfdir}/sysconfig/bcm43xx
%{_unitdir}/bcm43xx-bluetooth.service
%{_presetdir}/10-bcm43xx-bluetooth.preset
%dir /lib/firmware/brcm
/lib/firmware/brcm/bcm4329.hcd
/lib/firmware/brcm/bcm4330.hcd

%files bcm43xx-wifi-firmware
%dir /lib/firmware/brcm
/lib/firmware/brcm/brcmfmac4329.bin
/lib/firmware/brcm/brcmfmac4329-sdio.txt
/lib/firmware/brcm/brcmfmac4330.bin
/lib/firmware/brcm/brcmfmac4330-sdio.txt

%files vpu-firmware
%dir /lib/firmware/vpu
/lib/firmware/vpu/vpu_fw_imx6?.bin

%files mkbootlogo
%{_bindir}/greenconv
%{_bindir}/mkbootlogo
