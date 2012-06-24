Summary:     programs to access DOS disks w/o mounting them
Summary(de): Programme f�r den Zugriff auf DOS-Disks, ohne sie zu montieren 
Summary(fr): programmes pour acc�der aux disques DOS sans avoir � les monter
Summary(pl): Dost�p do dysk�w DOSa bez montowania
Summary(tr): Ba�lama (mount) yapmadan DOS disklerine eri�im sa�lar
Name:        mtools
Version:     3.9.1
Release:     3
Copyright:   GPL
Group:       Utilities/File
Group(pl):   Narz�dzia/Pliki
Source0:     http://www.tux.org/pub/tux/knaff/mtools/%{name}-%{version}.tar.gz 
Source1:     mtools.conf
Patch0:      mtools-info.patch
Patch1:      mtools-mzip.patch
URL:         http://www.tux.org/pub/tux/knaff/mtools/
Prereq:      /sbin/install-info
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Mtools is a collection of utilities to access MS-DOS disks from Unix without
mounting them. It supports Win'95 style long file names, OS/2 Xdf disks,
ZIP/JAZ disks and 2m disks (store up to 1992k on a high density 3 1/2 disk).

%description -l de
Mtools ist eine Dienstprogrammsammlung zum Zugriff auf MS-DOS-Disketten,
ohne da� diese montiert werden m�ssen. Es unterst�tzt Win'95-Dateinamen
(lang), OS/2-Xdf-, ZIP/JAZ- und 2m-Disketten (speichern bis zu 1992 KB auf
einer HD 3 1/2-Diskette).

%description -l fr
Mtools est un ensemble d'utilitaires pour acc�der aux disques MS-DOS depuis
UNIX sans les monter. Il supporte les noms longs Windows 95, les diques Xdf
OS/2, les disques ZIP et JAZ et les disques 2m (stockant 1992k sur une
disquette 3,5\").

%description -l pl
Mtools to zbi�r narz�dzi udost�pniaj�cych Unixowi DOSowe dyski bez ich
montowania. Obs�uguje d�ugie nazwy Win95, dyski Xdf z OS/2, dyski
ZIP/JAZ i dyski 2m (mieszcz�ce na 3.5-calowej dyskietce do 1992k).

%description -l tr
mtools, MS-DOS disklerine ba�lanmadan (mount edilmeden) UNIX sistemlerinden
eri�ilebilmesini sa�lar. Win'95 tarz� uzun dosya isimlerini, OS/2 Xdf
disklerini, ZIP/JAZ disklerini ve 2m disklerini destekler.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target_platform} \
	--prefix=/usr \
	--sysconfdir=/etc

make MYCFLAGS="$RPM_OPT_FLAGS -Wall"

(makeinfo --force mtools.texi; touch mtools.*)

strip mtools mkmanifest

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr,etc}

make prefix=$RPM_BUILD_ROOT/usr install

install %{SOURCE1} $RPM_BUILD_ROOT/etc
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/* \
	$RPM_BUILD_ROOT%{_mandir}/{man1,man5}/* \
	Changelog README Release.notes

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/mtools.info.gz /etc/info-dir

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/mtools.info.gz /etc/info-dir
fi

%files
%defattr(644,root,root,755)
%doc {Changelog,README,Release.notes}.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
%{_infodir}/*
%config /etc/mtools.conf
