Name: gstreamermm
Version: 1.4.3
Release: 1
Summary: C++ wrapper for GStreamer library
Group: System/Libraries
License: LGPLv2+
URL: http://www.gtkmm.org/
Source0: http://ftp.gnome.org/pub/GNOME/sources/gstreamermm/0.10/%{name}-%{version}.tar.xz
BuildRequires: pkgconfig(giomm-2.4) >= 2.28.0
BuildRequires: pkgconfig(gstreamer-1.0) >= 0.10.36
BuildRequires: pkgconfig(libxml++-2.6) >= 2.14
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0) >= 0.10.36
BuildRequires: doxygen graphviz m4

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
%setup -q

%build
%configure2_5x --enable-shared \
	--disable-dependency-tracking
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}-%{api}.so.%{major}
%{_libdir}/lib%{name}-%{api}.so.%{major}.*
%{_libdir}/lib%{name}_get_plugin_defs-%{api}.so.%{major}
%{_libdir}/lib%{name}_get_plugin_defs-%{api}.so.%{major}.*

%files -n %{develname}
%{_includedir}/gstreamermm-%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}-%{api}

%files doc
%doc COPYING
%doc %{_datadir}/doc/%{name}-%{api}
%doc %{_datadir}/devhelp/books/%{name}-%{api}/
