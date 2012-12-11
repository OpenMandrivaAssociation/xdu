%define name xdu
%define version 3.0
%define release %mkrel 10

Summary: Graphically display output of du command 
Name: %{name}
Version: %{version}
Release: %{release}
Source: ftp://ftp.arl.mil/pub/%{name}-%{version}.tar.bz2
License: BSD
Group: File tools
Url: http://sd.wareonearth.com/~phil/xdu/
Buildroot: %_tmppath/%{name}-root
BuildRequires: libx11-devel
BuildRequires: libxt-devel
BuildRequires: libxaw-devel
BuildRequires: imake
BuildRequires: gccmakedep

%description
Accepts output of du command on standard input and graphically
displays results in a window.

%prep
%setup -c 

%build
xmkmf -a
%make CXXOPTIONS="%optflags" EXTRA_LDOPTIONS="%ldflags"

%install
rm -fr $RPM_BUILD_ROOT

mkdir -p  $RPM_BUILD_ROOT%{_mandir}/man1/
cp %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
%makeinstall_std CONFDIR=%_datadir/X11

rm -fr %buildroot%_prefix/lib/X11

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/xdu
%_datadir/X11/app-defaults/XDu
%{_mandir}/man1/*
%doc README



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 3.0-10mdv2011.0
+ Revision: 634900
- simplify BR
- turn to standard prefix

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 3.0-9mdv2010.0
+ Revision: 435317
- BR libxp-devel
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.0-8mdv2009.0
+ Revision: 222660
- BuildRequires gccmakedep
- BuildRequires imake
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import xdu

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Sep 07 2006 Nicolas Lécureuil <neoclust@mandriva.org> 3.0-7mdv2007.0
- Add BuildRequires
- Fix File list

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.0-6mdk
- BuildRequires fix

* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.0-5mdk
- Rebuild

* Sat Jan 03 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.0-4mdk
- birthday rebuild

* Fri Dec 27 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.0-3mdk
- rebuild for rpm and glibc
- add forget config file

* Sun Aug 11 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.0-2mdk
- Add Buildrequires and Requires
- cleanup

* Sun Aug 11 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.0-1mdk
- 1st standalone mdk package

