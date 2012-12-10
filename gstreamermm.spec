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




%changelog
* Tue May 15 2012 Götz Waschk <waschk@mandriva.org> 0.10.10.2-1mdv2012.0
+ Revision: 798945
- update to new version 0.10.10.2

* Mon Feb 20 2012 Götz Waschk <waschk@mandriva.org> 0.10.10.1-1
+ Revision: 777938
- remove libtool archive
- new version
- update source URL

* Thu Jul 21 2011 Götz Waschk <waschk@mandriva.org> 0.10.10-1
+ Revision: 690828
- update to new version 0.10.10

* Thu Apr 28 2011 Götz Waschk <waschk@mandriva.org> 0.10.9.1-1
+ Revision: 659817
- update to new version 0.10.9.1

* Fri Apr 15 2011 Götz Waschk <waschk@mandriva.org> 0.10.9-1
+ Revision: 653099
- new version
- fix linking

* Sat Oct 16 2010 Götz Waschk <waschk@mandriva.org> 0.10.8-1mdv2011.0
+ Revision: 586002
- update to new version 0.10.8

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.10.7.3-1mdv2011.0
+ Revision: 550816
- update to new version 0.10.7.3

* Tue Apr 13 2010 Götz Waschk <waschk@mandriva.org> 0.10.7-1mdv2010.1
+ Revision: 534063
- update to new version 0.10.7

* Mon Dec 28 2009 Götz Waschk <waschk@mandriva.org> 0.10.6-1mdv2010.1
+ Revision: 482954
- new version
- new major

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 0.10.5.2-1mdv2010.0
+ Revision: 447186
- update to new version 0.10.5.2

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 0.10.5.1-1mdv2010.0
+ Revision: 439372
- new version
- split library package
- update file list
- fix installation

* Thu Sep 03 2009 Götz Waschk <waschk@mandriva.org> 0.10.5-1mdv2010.0
+ Revision: 427537
- update to new version 0.10.5

* Thu Aug 20 2009 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2010.0
+ Revision: 418390
- update to new version 0.10.4

* Wed Aug 19 2009 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdv2010.0
+ Revision: 418279
- update to new version 0.10.3

* Wed May 27 2009 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdv2010.0
+ Revision: 380292
- new version
- udpate file list

* Thu Feb 19 2009 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdv2009.1
+ Revision: 342797
- import gstreamermm


* Thu Feb 19 2009 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdv2009.1
- adapt Fedora spec

* Sun Dec 28 2008 Denis Leroy <denis@poolshark.org> - 0.9.8-2
- Rebuild for pkgconfig

* Fri Dec 26 2008 Denis Leroy <denis@poolshark.org> - 0.9.8-1
- Update to upstream 0.9.8
- Disabled parallel make

* Fri Oct 10 2008 Denis Leroy <denis@poolshark.org> - 0.9.7-1
- Update to upstream 0.9.7

* Wed Sep  3 2008 Denis Leroy <denis@poolshark.org> - 0.9.6-1
- Update to upstream 0.9.6

* Sat May 31 2008 Denis Leroy <denis@poolshark.org> - 0.9.5-1
- Update to upstream 0.9.5
- Fixed gstreamer plugin BuildRequires 

* Fri Feb 22 2008 Denis Leroy <denis@poolshark.org> - 0.9.4-1
- Updated to upstream 0.9.4

* Sun Feb 17 2008 Denis Leroy <denis@poolshark.org> - 0.9.2-1
- First draft

