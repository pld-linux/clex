Summary:	A file mananger
Summary(pl):	Zarz�dca plik�w
Name:		clex
Version:	3.13
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	http://www.clex.sk/download/%{name}-%{version}.tar.gz
# Source0-md5:	12e3840e3af83a65453b195463842da9
Patch0:		%{name}-ncurses.patch
URL:		http://www.clex.sk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLEX is an interactive full-screen file manager.

%description -l pl
CLEX jest interaktywnym, pe�noekranowym zarz�dc� plik�w.

%prep
%setup  -q
%patch0 -p1
#mv -f autoconf.h.bot config.h.bot

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
