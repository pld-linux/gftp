Summary:	Multithreaded FTP client for X Window
Summary(es.UTF-8):	Cliente FTP multithreaded para el X Window
Summary(ja.UTF-8):	X Window System 用マルチスレッド FTP クライアント
Summary(pl.UTF-8):	Wielowątkowy klient FTP dla X Window
Summary(pt_BR.UTF-8):	Cliente FTP multithreaded para o X Window
Summary(ru.UTF-8):	Многонитевый FTP клиент для X Window
Summary(uk.UTF-8):	Багатонитковий FTP клієнт для X Window
Name:		gftp
Version:	2.0.19
Release:	5
Epoch:		2
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://gftp.seul.org/%{name}-%{version}.tar.gz
# Source0-md5:	4c0cab4b35e8666f5892b02125270a21
Patch0:		%{name}-pld.patch
Patch1:		%{name}-no_libnsl.patch
Patch2:		%{name}-configure_in.patch
Patch3:		%{name}-desktop.patch
Patch4:		%{name}-gtk1_check.patch
URL:		http://gftp.seul.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gFTP is a multithreaded FTP client for X Window written using GTK+. It
features simultaneous downloads, resuming of interrupted file
transfers, file transfer queues, downloading of entire directories,
FTP proxy support, remote directory caching, passive and non-passive
file transfers, drag-n-drop support, bookmarks menu, stop button, and
many more features.

%description -l es.UTF-8
Cliente FTP multithreaded para el X Window.

%description -l ja.UTF-8
gFTP は X Window System 用のマルチスレッド FTP クライアントです。
gFTP は、複数ファイルの同時ダウンロードや、中断した転送の
レジューム、複数のファイルのダウンロード予約、ディレクトリごとの
ダウンロード、 FTP サイトのブックマーク、 FTP サイトのディレクトリ
のキャッシュ、ローカルとリモートのファイルのパーミッションの変更、
ドラッグアンドドロップ、コネクションマネージャ、その他いろいろな
機能を持っています。

%description -l pl.UTF-8
gFTP jest wielowątkowym klientem FTP dla X Window wykorzystującym
bibliotekę GTK+. Pozwala na jednoczesne ściąganie wielu plików,
wznawianie przerwanych transferów, kolejkowanie przesyłanych plików,
ściąganie zawartości katalogów, możliwość pracy z wykorzystaniem FTP
proxy, ściąganie plików w trybie pasywnym i nie-pasywnym, drag-n-drop,
zarządzanie połączeniami i wiele innych możliwości.

%description -l pt_BR.UTF-8
O gftp é um cliente FTP multithreaded para o X Window escrito usando a
biblioteca GTK+. Permite transferir arquivos simultâneamente, continuar
transferências interrompidas, filas para transferências de arquivos e
um gerenciador de conexões muito bom e muitas outras características.

%description -l ru.UTF-8
gFTP - многонитевый FTP клиент для X Window написаный с использованием
GTK. Среди его возможностей одновременная загрузка многих файлов,
продолжение прерваных передач файлов, очереди на передачу, загрузка
целых каталогов, поддержка FTP прокси, кеш индексов удаленных
каталогов, передача файлов в пасивном и непасивном режимах, поддержка
"буксирования" файлов (drag-n-drop), меню закладок, кнопка останова и
много другого.

%description -l uk.UTF-8
gFTP є багатонитковим FTP клієнтом для X Window, написаним з
використанням GTK. Серед його можливостей одночасні завантаження
багатьох файлів, продовження перерваних передач файлів, черги на
передачу, завантаження цілих каталогів, підтримка FTP проксі, кеш
індексів віддалених каталогів, передача файлів в пасивному та
непасивному режимах, підтримка "буксування" файлів (drag-n-drop), меню
закладинок, кнопка зупинки та багато іншого.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
rm -f aclocal.m4 acinclude.m4
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-textport
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_desktopdir} \
	Iconsdir=%{_pixmapsdir}

mv -f $RPM_BUILD_ROOT%{_bindir}/gftp{-gtk,}

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO THANKS docs/USERS-GUIDE ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/gftp
%{_datadir}/gftp/COPYING
%{_datadir}/gftp/*.xpm
%config %{_datadir}/gftp/gftprc
%config %{_datadir}/gftp/bookmarks
%{_desktopdir}/gftp.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/gftp.png
