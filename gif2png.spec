Summary:	tools for converting websites from using GIFs to using PNGs
Name:		gif2png
Version:	2.2.5
Release:	1
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Copyright:	BSD-like
Source:		http://www.tuxedo.org/~esr/gif2png/%{name}-%{version}.tar.gz
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
URL:		http://www.tuxedo.org/~esr/gif2png/
BuildRoot:	/tmp/%{name}-%{version}-root

%description 
Tools for converting GIFs to PNGs. The program gif2png converts GIF files
to PNG files. The Python script web2png converts an entire web tree, also
patching HTML pages to keep IMG SRC references correct.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README NEWS COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/bin/*
%{_mandir}/man1/*
