%define api 0.10
%define major 2
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
Name:           gstreamermm
Version:        0.10.1
Release:        %mkrel 1
Summary:        C++ wrapper for GStreamer library
Group:          Sound
License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
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

%package -n %develname
Summary:        Headers for developing programs that will use %{name}
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides: lib%name-devel = %version-%release


%description -n %develname
This package contains the static libraries and header files needed for
developing gstreamermm applications.


%prep
%setup -q

%build
export GST_INSPECT=%_bindir/gst-inspect-0.10
%configure2_5x --enable-shared --enable-docs --disable-dependency-tracking
# Parallel make not always working
make


%install
rm -rf $RPM_BUILD_ROOT installed-docs/
%makeinstall_std
# Move documentation to gtk-doc directory
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html
mv $RPM_BUILD_ROOT%{_docdir}/%{name}-0.10/docs/reference/html $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/%{name}-0.10

mv %buildroot%_datadir/doc/%name-%api installed-docs/

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


%files -n %develname
%defattr(-, root, root, -)
%doc ChangeLog
%doc installed-docs/*
%doc %{_datadir}/gtk-doc/html/%{name}-%api
%{_includedir}/gstreamermm-%api
%{_libdir}/*.so
%{_libdir}/*.la
%_libdir/%name-%api
%{_libdir}/pkgconfig/*.pc


