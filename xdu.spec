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

