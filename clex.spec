Summary:	A file mananger
Summary(pl):	Mened¿er plików
Name:		clex
Version:	3.1.6
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://www.clex.sk/download/%{name}-%{version}.src.tar.gz
Patch0:		%{name}-ncurses.patch
URL:		http://www.clex.sk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLEX is an interactive full-screen file manager.

%description -l pl
CLEX jest interaktywnym, pe³noekranowym mened¿erem plików.

%prep
%setup  -q
%patch0 -p1

%build
mv -f autoconf.h.bot config.h.bot
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
