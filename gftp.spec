#TODO
# - PLD Bookmarks
Summary:	Multithreaded FTP client for X Window
Summary(es):	Cliente FTP multithreaded para el X Window
Summary(ja):	X Window System мя╔ч╔К╔а╔╧╔Л╔ц╔и FTP ╔╞╔И╔╓╔╒╔С╔х
Summary(pl):	Wielow╠tkowy klient FTP dla X Window
Summary(pt_BR):	Cliente FTP multithreaded para o X Window
Summary(ru):	Многонитевый FTP клиент для X Window
Summary(uk):	Багатонитковий FTP кл╕╓нт для X Window
Name:		gftp
Version:	2.0.15
Release:	1
Epoch:		2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://gftp.seul.org/%{name}-%{version}.tar.gz
# Source0-md5:	5a076c251c1d81cace49ebe197c0d70a
Patch0:		%{name}-pld.patch
Patch1:		%{name}-no_libnsl.patch
Patch2:		%{name}-configure_in.patch
Patch3:		%{name}-desktop.patch
URL:		http://gftp.seul.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gFTP is a multithreaded FTP client for X Window written using Gtk. It
features simultaneous downloads, resuming of interrupted file
transfers, file transfer queues, downloading of entire directories,
ftp proxy support, remote directory caching, passive and non-passive
file transfers, drag-n-drop support, bookmarks menu, stop button, and
many more features.

%description -l es
Cliente FTP multithreaded para el X Window.

%description -l ja
gFTP ╓о X Window System мя╓н╔ч╔К╔а╔╧╔Л╔ц╔и FTP ╔╞╔И╔╓╔╒╔С╔х╓г╓╧║ё
gFTP ╓о║╒йё©Т╔у╔║╔╓╔К╓нф╠╩Ч╔ю╔╕╔С╔М║╪╔и╓Д║╒цФцг╓╥╓©е╬аВ╓н
╔Л╔╦╔Е║╪╔Ю║╒йё©Т╓н╔у╔║╔╓╔К╓н╔ю╔╕╔С╔М║╪╔им╫лС║╒╔г╔ё╔Л╔╞╔х╔Й╓╢╓х╓н
╔ю╔╕╔С╔М║╪╔и║╒ FTP ╔╣╔╓╔х╓н╔ж╔ц╔╞╔ч║╪╔╞║╒ FTP ╔╣╔╓╔х╓н╔г╔ё╔Л╔╞╔х╔Й
╓н╔╜╔Ц╔ц╔╥╔Е║╒╔М║╪╔╚╔К╓х╔Й╔Б║╪╔х╓н╔у╔║╔╓╔К╓н╔я║╪╔ъ╔ц╔╥╔Г╔С╓нйя╧╧║╒
╔и╔И╔ц╔╟╔╒╔С╔и╔и╔М╔ц╔в║╒╔Ё╔м╔╞╔╥╔Г╔С╔ч╔м║╪╔╦╔Ц║╒╓╫╓нб╬╓╓╓М╓╓╓М╓й
╣║г╫╓Р╩Щ╓ц╓ф╓╓╓ч╓╧║ё

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
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing aclocal.m4 acinclude.m4
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
	Utilitiesdir=%{_applnkdir}/Network/FTP \
	Iconsdir=%{_pixmapsdir}

mv -f $RPM_BUILD_ROOT%{_bindir}/gftp{-gtk,}

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
%{_applnkdir}/Network/FTP/gftp.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/gftp.png
