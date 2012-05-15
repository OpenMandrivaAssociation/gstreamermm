%define api 0.10
%define major 2
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
%define gpdmajor %major
%define libnamegetplugindefs %mklibname %{name}-get-plugin-defs %api %gpdmajor
Name:           gstreamermm
Version:        0.10.10.2
Release:        %mkrel 1
Summary:        C++ wrapper for GStreamer library
Group:          Sound
License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
Patch0:		gstreamermm-0.10.9-fix-linking.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glibmm2.4-devel >= 2.16.0
BuildRequires: gtkmm2.4-devel >= 2.12.0
BuildRequires: gstreamer0.10-devel >= 0.10.22
BuildRequires: libgstreamer-plugins-base-devel >= 0.10.22
BuildRequires: libxml++-devel >= 2.14.0
BuildRequires: doxygen graphviz


%description
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.

%package -n %libname
Summary:        C++ wrapper for GStreamer library
Group:          System/Libraries

%description -n %libname
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.

%package -n %libnamegetplugindefs
Summary:        C++ wrapper for GStreamer library
Group:          System/Libraries

%description -n %libnamegetplugindefs
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.

%package -n %develname
Summary:        Headers for developing programs that will use %{name}
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Requires:	%libnamegetplugindefs = %{version}-%{release}
Provides: lib%name-devel = %version-%release


%description -n %develname
This package contains the static libraries and header files needed for
developing gstreamermm applications.


%prep
%setup -q
%apply_patches
autoreconf -fi

%build
export GST_INSPECT=%_bindir/gst-inspect-0.10
%configure2_5x --enable-shared --enable-docs --disable-dependency-tracking
# Parallel make not always working
make


%install
rm -rf $RPM_BUILD_ROOT installed-docs/
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdvver < 200900
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-, root, root, -)
%doc AUTHORS NEWS README
%{_libdir}/libgstreamermm-%api.so.%{major}*

%files -n %libnamegetplugindefs
%defattr(-, root, root, -)
%{_libdir}/libgstreamermm_get_plugin_defs-%api.so.%{gpdmajor}*

%files -n %develname
%defattr(-, root, root, -)
%doc ChangeLog
%_datadir/devhelp/books/%name-%api
%doc %{_datadir}/doc/%name-%api
%{_includedir}/gstreamermm-%api
%{_libdir}/*.so
%_libdir/%name-%api
%{_libdir}/pkgconfig/*.pc


