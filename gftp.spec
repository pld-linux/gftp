Summary:	Multithreaded FTP client for X Window
Summary(es):	Cliente FTP multithreaded para el X Windows
Summary(pl):	Wielow±tkowy klient FTP dla X Window
Summary(pt_BR):	Cliente FTP multithreaded para o X Window
Name:		gftp
Version:	2.0.10
Release:	1
Epoch:		2
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
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
gFTP jest wielow±tkowym klientem FTP dla X Window wykorzystuj±cym
bibliotekê gtk+. Pozwala na jednoczesne ¶ci±ganie wielu plików,
wznawianie przerwanych transferów, kolejkowanie przesy³anych plików,
¶ci±ganie zawarto¶ci katalogów, mo¿liwo¶æ pracy z wykorzystaniem ftp
proxy, ¶ci±gnie plików w trybie passiv i non-passive, drag-n-drop,
zarz±dzanie po³±czeniami i wiele innych mo¿liwo¶ci.

%description -l pt_BR
O gftp é um cliente FTP multithreaded para o X Window escrito usando a
biblioteca gtk. Permite transferir arquivos simultâneamente, continuar
transferências interrompidas, filas para transferências de arquivos e
um gerenciador de conexões muito bom e muitas outras características.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
gettextize --copy --force
aclocal
autoconf
automake -a -c
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
