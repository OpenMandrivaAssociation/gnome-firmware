%global uuid    org.gnome.Firmware
%global tarball_version %%(echo %{version} | tr '~' '.')
 
Name:           gnome-firmware
Version:        46.0
Release:        1
Summary:        Install firmware on devices
Group:          System/Firmware 
License:        GPLv2+
URL:            https://gitlab.gnome.org/hughsie/gnome-firmware
Source0:        https://people.freedesktop.org/~hughsient/releases/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  help2man
BuildRequires:  appstream-util
BuildRequires:  meson
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(fwupd) >= 1.2.10
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.6.0
BuildRequires:  pkgconfig(xmlb) >= 0.1.7
BuildRequires:  pkgconfig(libadwaita-1)
Requires:       hicolor-icon-theme
 
%description
This application can:
 
- Upgrade, downgrade and reinstall firmware on devices supported by fwupd.
- Unlock locked fwupd devices
- Verify firmware on supported devices
- Display all releases for a fwupd device
 
%prep
%autosetup -p1 -n %{name}-%{tarball_version}
 
%build
%meson -Dman=true
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
 
%files -f %{name}.lang
%license COPYING
%doc README.md MAINTAINERS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/*.1.*
%{_metainfodir}/*.xml
