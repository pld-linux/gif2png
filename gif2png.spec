Summary:	tools for converting websites from using GIFs to using PNGs
Summary(es):	Herramienta para convertir sitios y imagenes de GIFs hacia PNGs
Summary(fr):	Outils de conversion de sites: convertit les GIFs en PNGs
Summary(pl):	Narzêdzia do konwersji plików GIF na pliki PNG
Summary(pt_BR):	Ferramentas para a conversão de arquivos no formato GIF para PNG
Name:		gif2png
Version:	2.4.4
Release:	1
License:	BSD-like
Group:		Applications/Graphics
Source0:	http://www.tuxedo.org/~esr/gif2png/%{name}-%{version}.tar.gz
URL:		http://www.tuxedo.org/~esr/gif2png/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel >= 1.0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for converting GIFs to PNGs. The program gif2png converts GIF
files to PNG files. The Python script web2png converts an entire web
tree, also patching HTML pages to keep IMG SRC references correct.

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

%description -l pl
Narzêdzia do konwersji plików GIF do formatu PNG. Program gif2png
konwertuje pliki GIF do formatu PNG. Pythonowy skrypt web2png
konwertuje ca³e drzewo witryny WWW, poprawiaj±c jednocze¶nie odno¶niki
IMG SRC w stronach HTML.

%description -l pt_BR
Ferramentas para conversão de GIFs para PNG. O programa gif2png
converte arquivos no formato GIF para o formato PNG. O roteiro em
python web2png converte automaticamente vários arquivos em seus
sub-diretórios, assim como modifica as páginas HTML mantendo as
referência IMG SRC.

%prep
%setup -q

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure CPPFLAGS="$CPPFLAGS"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS COPYING
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
