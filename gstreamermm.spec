Name: gstreamermm
Version: 1.10.0
Release: 1
Summary: C++ wrapper for GStreamer library
Group: System/Libraries
License: LGPLv2+
URL: https://www.gtkmm.org/
Source0: http://ftp.gnome.org/pub/GNOME/sources/gstreamermm/1.10/%{name}-%{version}.tar.xz
Patch0:		gstreamermm-1.8.0-cast.patch
Patch1:		0001-Fix-build-against-glib-2.68.patch
BuildRequires:	pkgconfig(giomm-2.4) >= 2.36.0
BuildRequires:	pkgconfig(gstreamer-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-app-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-audio-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-base-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-check-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-controller-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-fft-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-net-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-riff-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-rtp-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-sdp-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-tag-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gstreamer-video-1.0) >= 1.4.3
BuildRequires:	pkgconfig(gtkmm-3.0) >= 3.0
BuildRequires:	doxygen
BuildRequires:	m4

%description
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org). It is designed to allow
C++ development of applications that work with multi-media.

%define api 1.0
%define major 0
%define libname %mklibname %name %api %major

%package -n %libname
Summary: C++ wrapper for GStreamer library
Group: System/Libraries

%description -n %libname
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org). It is designed to allow
C++ development of applications that work with multi-media.

%define develname %mklibname %name -d
%package -n %develname
Summary: Headers for developing programs that will use %{name}
Group: Development/C++
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}

%description -n %develname
This package contains the static libraries and header files needed for
developing gstreamermm applications.

%package doc
Summary: Developer's documentation for the gstreamermm library
Group: Development/Other
BuildArch: noarch

%description doc
This package contains developer's documentation for the GStreamermm
library. Gstreamermm is the C++ API for the GStreamer library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
%configure --enable-shared \
	--disable-dependency-tracking
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING NEWS README
#{_libdir}/lib%{name}-%{api}.so.%{major}
#{_libdir}/lib%{name}-%{api}.so.%{major}.*
#{_libdir}/lib%{name}_get_plugin_defs-%{api}.so.%{major}
#{_libdir}/lib%{name}_get_plugin_defs-%{api}.so.%{major}.*

%files -n %{develname}
#{_includedir}/gstreamermm-%{api}
#{_libdir}/*.so
#{_libdir}/pkgconfig/*.pc
#{_libdir}/%{name}-%{api}

%files doc
%doc COPYING
%doc %{_datadir}/doc/%{name}-%{api}
%doc %{_datadir}/devhelp/books/%{name}-%{api}/
