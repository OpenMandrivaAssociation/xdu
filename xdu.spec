%define name xdu
%define version 3.0
%define release %mkrel 9

Summary: Graphically display output of du command 
Name: %{name}
Version: %{version}
Release: %{release}
Source: ftp://ftp.arl.mil/pub/%{name}-%{version}.tar.bz2
License: BSD
Group: File tools
Url: http://sd.wareonearth.com/~phil/xdu/
Buildroot: %_tmppath/%{name}-root
BuildRequires: X11-devel
# needed for rman
BuildRequires: xorg-x11 imake gccmakedep libxp-devel
BuildRequires: lesstif-devel 
Requires: fileutils

%description
Accepts output of du command on standard input and graphically
displays results in a window.

%prep
%setup -c 

%build
xmkmf -a
%make

%install
rm -fr $RPM_BUILD_ROOT

mkdir -p  $RPM_BUILD_ROOT%{_mandir}/man1/
cp %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
%makeinstall_std

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/X11/app-defaults/XDu
%_bindir/xdu
%_prefix/lib/X11/app-defaults
%{_mandir}/man1/*
%doc README

