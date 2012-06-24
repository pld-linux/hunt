Summary:	Connection intruder
Summary(pl):	Przechwytywasz/sniffer po��cze�
Name:		hunt
Version:	1.5
Release:	2
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://ftp.gncz.cz/pub/linux/hunt/%{name}-%{version}.tgz
# Source0-md5:	5a8886784d1668a8518d5562bfd01ae7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hunt is a program for intruding into a connection, watching it and
resetting it.

%description -l pl
Hunt to program do przechwytywania, podgl�dania oraz przerywania
po��cze� sieciowych.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -D_REENTRANT" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install man/hunt.1 $RPM_BUILD_ROOT%{_mandir}/man1
install hunt $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* TODO
%attr(755,root,root) %{_bindir}/hunt
%{_mandir}/man1/*
