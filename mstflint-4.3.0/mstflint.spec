%{!?ibmadlib: %define ibmadlib libibmad-devel}
%{!?name: %define name mstflint}
%{!?version: %define version 4.3.0}
%{!?release: %define release 1}
%{!?buildtype: %define buildtype "native"}
%{!?noinband: %define noinband 0}
%{!?nodc: %define nodc 0}
%{!?enablecs: %define enablecs 0}

%define debug_package %{nil}
%define optflags -g -O2

Summary: Mellanox firmware burning application
Name: %{name}
Version: 4.3.0
Release: 1
License: GPL/BSD
Url: http://openfabrics.org
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source: http://www.openfabrics.org/downloads/mstflint-4.3.0.tar.gz
ExclusiveArch: i386 i486 i586 i686 x86_64 ia64 ppc ppc64 ppc64le arm64 aarch64
BuildRequires: zlib-devel %{ibmadlib}

%description
This package contains firmware update tool, vpd dump and register dump tools
for network adapters based on Mellanox Technologies chips.

%prep
%setup -q

%build

%if %{nodc}
    config_flags="$config_flags --disable-dc"
%endif

%if %{noinband}
    config_flags="$config_flags --disable-inband"
%endif

%if %{enablecs}
    config_flags="$config_flags --enable-cs"
%endif

%if %{buildtype} == "ppc"
    config_flags="$config_flags --host=ppc-linux"
%endif

%if %{buildtype} == "ppc64"
    config_flags="$config_flags --host=ppc64-linux --enable-static-libstdcpp=yes"
%endif

%if %{buildtype} == "ppc64le"
    config_flags="$config_flags --host=powerpc64le-linux-gnu --enable-dynamic-ld=yes"
%endif

%if %{buildtype} == "arm64"
    config_flags="$config_flags --host arm"
%endif

%configure ${config_flags}

make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/mstmread
%{_bindir}/mstmwrite
%{_bindir}/mstflint
%{_bindir}/mstregdump
%{_bindir}/mstmtserver
%{_bindir}/mstvpd
%{_bindir}/mstmcra
%{_bindir}/mstconfig
%{_bindir}/hca_self_test.ofed
%{_includedir}/mtcr_ul/mtcr.h
%{_libdir}/libmtcr_ul.a
%{_datadir}/mstflint
%{_mandir}/man1/*

%changelog
* Mon Jan 11 2016 Adrian Chiris <adrianc@dev.mellanox.co.il>
   MFT 4.3.0 Updates

* Wed Aug 26 2015 Adrian Chiris <adrianc@dev.mellanox.co.il>
   MFT 4.1.0 Updates
   
* Wed Jun 05 2015 Adrian Chiris <adrianc@dev.mellanox.co.il>
   MFT 4.0.1 Updates

* Thu Feb 05 2015 Adrian Chiris <adrianc@dev.mellanox.co.il>
   MFT 4.0.0 Updates

* Sun Dec 07 2014 Tomer Cohen <tomerc@mellanox.com>
   Added support for multiple architectures

* Mon Oct 12 2014 Oren Kladnitsky <orenk@dev.mellanox.co.il>
   MFT 3.7.1

* Mon Jul 31 2014 Oren Kladnitsky <orenk@dev.mellanox.co.il>
   MFT 3.7.0 Updates

* Mon Mar 31 2014 Oren Kladnitsky <orenk@dev.mellanox.co.il>
   MFT 3.6.0 Updates

* Tue Dec 24 2013 Oren Kladnitsky <orenk@dev.mellanox.co.il>
   MFT 3.5.0 Updates

* Wed Mar 20 2013 Oren Kladnitsky <orenk@dev.mellanox.co.il>
   MFT 3.0.0

* Thu Dec  4 2008 Oren Kladnitsky <orenk@dev.mellanox.co.il>
   Added hca_self_test.ofed installation
   
* Fri Dec 23 2007 Oren Kladnitsky <orenk@dev.mellanox.co.il>
   Added mtcr.h installation
   
* Fri Dec 07 2007 Ira Weiny <weiny2@llnl.gov> 1.0.0
   initial creation

