Summary:	Multithreaded FTP client for X Window
Summary(es):	Cliente FTP multithreaded para el X Windows
Summary(pl):	Wielow╠tkowy klient FTP dla X Window
Summary(pt_BR):	Cliente FTP multithreaded para o X Window
Summary(ru):	Многонитевый FTP клиент для X Window
Summary(uk):	Багатонитковий FTP кл╕╓нт для X Window
Name:		gftp
Version:	2.0.11
Release:	2
Epoch:		2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://gftp.seul.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-pld.patch
Patch1:		%{name}-no_libnsl.patch
URL:		http://gftp.seul.org/
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
gFTP is a multithreaded FTP client for X Windows written using Gtk. It
features simultaneous downloads, resuming of interrupted file
transfers, file transfer queues, downloading of entire directories,
ftp proxy support, remote directory caching, passive and non-passive
file transfers, drag-n-drop support, bookmarks menu, stop button, and
many more features.

%description -l es
Cliente FTP multithreaded para el X Windows.

%description -l pl
gFTP jest wielow╠tkowym klientem FTP dla X Window wykorzystuj╠cym
bibliotekЙ gtk+. Pozwala na jednoczesne ╤ci╠ganie wielu plikСw,
wznawianie przerwanych transferСw, kolejkowanie przesyЁanych plikСw,
╤ci╠ganie zawarto╤ci katalogСw, mo©liwo╤Ф pracy z wykorzystaniem ftp
proxy, ╤ci╠gnie plikСw w trybie passiv i non-passive, drag-n-drop,
zarz╠dzanie poЁ╠czeniami i wiele innych mo©liwo╤ci.

%description -l pt_BR
O gftp И um cliente FTP multithreaded para o X Window escrito usando a
biblioteca gtk. Permite transferir arquivos simultБneamente, continuar
transferЙncias interrompidas, filas para transferЙncias de arquivos e
um gerenciador de conexУes muito bom e muitas outras caracterМsticas.

%description -l ru
gFTP - многонитевый FTP клиент для X Window написаный с использованием
GTK. Среди его возможностей одновременная загрузка многих файлов,
продолжение прерваных передач файлов, очереди на передачу, загрузка
целых каталогов, поддержка ftp прокси, кеш индексов удаленных
каталогов, передача файлов в пасивном и непасивном режимах, поддержка
"буксирования" файлов (drag-n-drop), меню закладок, кнопка останова и
много другого.

%description -l uk
gFTP ╓ багатонитковим FTP кл╕╓нтом для X Window, написаним з
використанням GTK. Серед його можливостей одночасн╕ завантаження
багатьох файл╕в, продовження перерваних передач файл╕в, черги на
передачу, завантаження ц╕лих каталог╕в, п╕дтримка ftp прокс╕, кеш
╕ндекс╕в в╕ддалених каталог╕в, передача файл╕в в пасивному та
непасивному режимах, п╕дтримка "буксування" файл╕в (drag-n-drop), меню
закладинок, кнопка зупинки та багато ╕ншого.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
gettextize --copy --force
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/Network/FTP

gzip -9nf README TODO THANKS docs/USERS-GUIDE ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz docs/*.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/gftp
%{_datadir}/gftp/*.xpm
%{_datadir}/gftp/COPYING
%config %{_datadir}/gftp/gftprc
%config %{_datadir}/gftp/bookmarks

%{_pixmapsdir}/gftp.png
%{_mandir}/man1/*

%{_applnkdir}/Network/FTP/gftp.desktop
