Summary:	Connection intruder
Name:		hunt
Version:	1.5
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.gncz.cz/pub/linux/hunt/%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hunt is a program for intruding into a connection, watching it and
resetting it.

Please make sure you KNOW what you are doing before using hunt.
It is recommended that you should test how it behaves on some test
connections and then use it wisely.

%prep
%setup -q

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS -Wall -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install man/hunt.1 $RPM_BUILD_ROOT%{_mandir}/man1
install hunt $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/hunt
%{_mandir}/man1/*
