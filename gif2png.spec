Summary:	tools for converting websites from using GIFs to using PNGs
Summary(es):	Herramienta para convertir sitios y imagenes de GIFs hacia PNGs
Summary(fr):	Outils de conversion de sites: convertit les GIFs en PNGs
Name:		gif2png
Version:	2.3.2
Release:	1
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
License:	BSD-like
Source0:	http://www.tuxedo.org/~esr/gif2png/%{name}-%{version}.tar.gz
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
URL:		http://www.tuxedo.org/~esr/gif2png/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Tools for converting GIFs to PNGs. The program gif2png converts GIF
files to PNG files. The Python script web2png converts an entire web
tree, also patching HTML pages to keep IMG SRC references correct.

%description -l pl
Narzêdzia do konwersji plików GIF do formatu PNG. Program gif2png
konwertuje pliki GIF do formatu PNG. Pythonowy skrypt web2png
konwertuje ca³e drzewo witryny WWW, poprawiaj±c jednocze¶nie odno¶niki
IMG SRC w stronach HTML.

%description -l es
Herramienta de conversion GIF hacia PNG. El programa gif2png convierte
los archivos GIF al formato PNG. El script Python convierte un arbol
web completo y modifica incluso las paginas html para poner al dia las
referencias a imagenes <IMG SRC ...>.

%description -l fr
Outil de conversion du format GIF au format PNG. Le programme gif2png
convertit les fichiers GIF au format PNG. Le script Python scanne une
arborescence web complete et modifie aussi les pages HTML afin de
référencer à nouveau les fichiers images <IMG SRC ...>.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README NEWS COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
