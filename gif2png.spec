Summary:	Tools for converting websites from using GIFs to using PNGs
Summary(es.UTF-8):	Herramienta para convertir sitios y imagenes de GIFs hacia PNGs
Summary(fr.UTF-8):	Outils de conversion de sites: convertit les GIFs en PNGs
Summary(pl.UTF-8):	Narzędzia do konwersji plików GIF na pliki PNG
Summary(pt_BR.UTF-8):	Ferramentas para a conversão de arquivos no formato GIF para PNG
Name:		gif2png
Version:	3.0.3
Release:	1
License:	BSD-like
Group:		Applications/Graphics
Source0:	http://catb.org/~esr/gif2png/%{name}-%{version}.tar.gz
# Source0-md5:	5f109edd79276d2245d2269446e4c4bd
Source1:	%{name}-%{version}-vendor.tar.xz
# Source1-md5:	2a298b30376beb82f995487d3bace8d8
Patch0:		%{name}-go.sum.patch
URL:		http://catb.org/~esr/gif2png/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	golang
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	xmlto
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch %{ix86}
%define GOARCH 386
%endif
%ifarch %{x8664}
%define GOARCH amd64
%endif

%description
Tools for converting GIFs to PNGs. The program gif2png converts GIF
files to PNG files. The Python script web2png converts an entire web
tree, also patching HTML pages to keep IMG SRC references correct.

%description -l es.UTF-8
Herramienta de conversion GIF hacia PNG. El programa gif2png convierte
los archivos GIF al formato PNG. El script Python convierte un arbol
web completo y modifica incluso las paginas html para poner al dia las
referencias a imagenes <IMG SRC ...>.

%description -l fr.UTF-8
Outil de conversion du format GIF au format PNG. Le programme gif2png
convertit les fichiers GIF au format PNG. Le script Python scanne une
arborescence web complete et modifie aussi les pages HTML afin de
référencer à nouveau les fichiers images <IMG SRC ...>.

%description -l pl.UTF-8
Narzędzia do konwersji plików GIF do formatu PNG. Program gif2png
konwertuje pliki GIF do formatu PNG. Pythonowy skrypt web2png
konwertuje całe drzewo witryny WWW, poprawiając jednocześnie odnośniki
IMG SRC w stronach HTML.

%description -l pt_BR.UTF-8
Ferramentas para conversão de GIFs para PNG. O programa gif2png
converte arquivos no formato GIF para o formato PNG. O roteiro em
python web2png converte automaticamente vários arquivos em seus
sub-diretórios, assim como modifica as páginas HTML mantendo as
referência IMG SRC.

%prep
%setup -q -b1
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' web2png

%build
export GOARCH=%{GOARCH}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README gif2png-logo.png
%attr(755,root,root) %{_bindir}/gif2png
%attr(755,root,root) %{_bindir}/web2png
%{_mandir}/man1/gif2png.1*
%{_mandir}/man1/web2png.1*
