Summary:	A file mananger
Summary(pl):	Zarz±dca plików
Name:		clex
Version:	3.1.8
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	http://www.clex.sk/download/%{name}-%{version}.src.tar.gz
# Source0-md5:	a4c9f7d169f4fadb40ed7582ee2dd2f3
Patch0:		%{name}-ncurses.patch
URL:		http://www.clex.sk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLEX is an interactive full-screen file manager.

%description -l pl
CLEX jest interaktywnym, pe³noekranowym zarz±dc± plików.

%prep
%setup  -q
%patch0 -p1
mv -f autoconf.h.bot config.h.bot

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
