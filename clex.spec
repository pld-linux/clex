Summary:	A file mananger
Summary(pl):	Mened¿er plików
Name:		clex
Version:	3.1.2
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://www.clex.sk/download/%{name}-%{version}.tar.gz
URL:		http://www.clex.sk
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

%build
aclocal
autoconf
automake -a -c -f
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/clex
%{_mandir}/man*/*
