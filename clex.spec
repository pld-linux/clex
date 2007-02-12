Summary:	A file mananger
Summary(pl.UTF-8):	Zarządca plików
Name:		clex
Version:	3.14
Release:	1
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://www.clex.sk/download/%{name}-%{version}.tar.gz
# Source0-md5:	8ed86b6e50266a3b2c7419e369e3ec03
Patch0:		%{name}-ncurses.patch
URL:		http://www.clex.sk/about.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLEX is an interactive full-screen file manager.

%description -l pl.UTF-8
CLEX jest interaktywnym, pełnoekranowym zarządcą plików.

%prep
%setup  -q
%patch0 -p1

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
