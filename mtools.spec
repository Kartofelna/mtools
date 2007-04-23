%define _snap	20070411
Summary:	Programs to access DOS disks w/o mounting them
Summary(de.UTF-8):	Programme für den Zugriff auf DOS-Disks, ohne sie zu montieren
Summary(es.UTF-8):	Programas para acceder discos DOS sin montarlos
Summary(fr.UTF-8):	Programmes pour accéder aux disques DOS sans avoir à les monter
Summary(pl.UTF-8):	Dostęp do dysków DOS-a bez montowania
Summary(pt_BR.UTF-8):	Programas para acessar discos DOS sem montá-los
Summary(tr.UTF-8):	Bağlama (mount) yapmadan DOS disklerine erişim sağlar
Name:		mtools
Version:	3.9.10
Release:	1.%{_snap}.1
License:	GPL
Group:		Applications/File
Source0:	http://mtools.linux.lu/%{name}-%{version}.tar.bz2
# Source0-md5:	0d0eb50a52eaf2e1921e1a61bab09be7
Source1:	%{name}.conf
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	7af7d462db97b53e4bfdc4aa1e41b516
Source3:	http://mtools.linux.lu/%{name}-%{version}-%{_snap}.diff.gz
# Source3-md5:	587b808a689093f6fb64ab1990ffbef1
Patch0:		%{name}-info.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-no_libnsl_and_libbsd.patch
Patch3:		%{name}-pmake.patch
URL:		http://mtools.linux.lu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mtools is a collection of utilities to access MS-DOS disks from Unix
without mounting them. It supports Win'95 style long file names, OS/2
Xdf disks, ZIP/JAZ disks and 2m disks (store up to 1992k on a high
density 3 1/2 disk).

%description -l de.UTF-8
Mtools ist eine Dienstprogrammsammlung zum Zugriff auf
MS-DOS-Disketten, ohne daß diese montiert werden müssen. Es
unterstützt Win'95-Dateinamen (lang), OS/2-Xdf-, ZIP/JAZ- und
2m-Disketten (speichern bis zu 1992 KB auf einer HD 3 1/2-Diskette).

%description -l es.UTF-8
Mtools es una colección de utilitarios para acceder a discos MS-DOS en
Unix sin montarlos. Soporta nombres largos de archivos estilo Win'95,
discos OS/2 Xdf, discos ZIP/JAZ y discos 2m (almacena hasta 1992k en
un disco 3 1/2 de alta densidad).

%description -l fr.UTF-8
Mtools est un ensemble d'utilitaires pour accéder aux disques MS-DOS
depuis UNIX sans les monter. Il supporte les noms longs Windows 95,
les diques Xdf OS/2, les disques ZIP et JAZ et les disques 2m
(stockant 1992k sur une disquette 3,5\").

%description -l pl.UTF-8
Mtools to zbiór narzędzi udostępniających Uniksowi DOS-owe dyski bez
ich montowania. Obsługuje długie nazwy Win95, dyski Xdf z OS/2, dyski
ZIP/JAZ i dyski 2m (mieszczące na 3.5-calowej dyskietce do 1992k).

%description -l pt_BR.UTF-8
Mtools é uma coleção de utilitários para acessar discos MS-DOS no Unix
sem montá-los. Ele suporta nomes longos de arquivos estilo Win'95,
discos OS/2 Xdf, discos ZIP/JAZ e discos 2m (armazena até 1992k em um
disco 3 1/2 de alta densidade).

%description -l tr.UTF-8
mtools, MS-DOS disklerine bağlanmadan (mount edilmeden) UNIX
sistemlerinden erişilebilmesini sağlar. Win'95 tarzı uzun dosya
isimlerini, OS/2 Xdf disklerini, ZIP/JAZ disklerini ve 2m disklerini
destekler.

%package floppyd
Summary:	floppyd - daemon for remote access to floppy drive
Summary(pl.UTF-8):	floppyd - serwer zdalnego dostępu do stacji dyskietek
Summary(pt_BR.UTF-8):	Daemon para acesso remoto a um drive de disquete
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description floppyd
floppy daemon for remote access to floppy drive. floppyd_installtest -
tests whether floppyd is installed and running

%description floppyd -l pl.UTF-8
Demon floppy do zdalnego dostępu do napędu dyskietek.
floppyd_installtest - sprawdza, czy floppyd jest zainstalowany i
działa.

%description floppyd -l pt_BR.UTF-8
Daemon para acesso remoto a um drive de disquete.

%prep
%setup -q
gunzip -c %{SOURCE3} | patch -p1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp /usr/share/automake/config.sub .
%{__autoconf}
%configure

%{__make} \
	MYCFLAGS="%{rpmcflags} -Wall"

makeinfo --force mtools.texi
touch mtools.*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_sysconfdir}} \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

tar -xjf %{SOURCE2} -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/README.mtools-non-english-man-pages.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc Changelog README Release.notes
%attr(755,root,root) %{_bindir}/amuFormat.sh
%attr(755,root,root) %{_bindir}/m*
%attr(755,root,root) %{_bindir}/tgz
%attr(755,root,root) %{_bindir}/uz
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mtools.conf
%{_mandir}/man[15]/m*
%lang(de) %{_mandir}/de/man[15]/m*
%lang(es) %{_mandir}/es/man[15]/m*
%lang(fi) %{_mandir}/fi/man[15]/m*
%lang(fr) %{_mandir}/fr/man[15]/m*
%lang(it) %{_mandir}/it/man[15]/m*
%lang(pl) %{_mandir}/pl/man[15]/m*
%{_infodir}/*info*

%files floppyd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/floppyd*
%{_mandir}/man[15]/f*
