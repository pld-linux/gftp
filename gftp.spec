Summary:	Multithreaded FTP client for X Window
Summary(pl):	Wielow±tkowy klient FTP dla X Window
Name:		gftp
Version:	2.0.6a
Release:	1
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Copyright:	GPL
Source0:	http://gftp.seul.org/%{name}-%{version}.tar.gz
Patch0:		gftp-pld.patch
Patch1:		gftp-applnkdir.patch
URL:		http://gftp.seul.org/
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	glib-devel >= 1.2.3
BuildRequires:	XFree86-devel
BuildRequires:	gettext-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6
%define		_applnkdir	%{_datadir}/applnk

%description
gFTP is a multithreaded FTP client for X Windows written using Gtk. It
features simultaneous downloads, resuming of interrupted file transfers,
file transfer queues, downloading of entire directories, ftp proxy support,
remote directory caching, passive and non-passive file transfers,
drag-n-drop support, bookmarks menu, stop button, and many more features.

%description -l pl
gFTP jest wielow±tkowym klientem FTP dla X Window wykorzystuj±cym bibliotekê
gtk+. Pozwala na jednoczesne ¶ci±ganie wielu plików, wznawianie przerwanych
transferów, kolejkowanie przesy³anych plików, ¶ci±ganie zawarto¶ci
katalogów, mo¿liwo¶æ pracy z wykorzystaniem ftp proxy, ¶ci±gnie plików w
trybie passiv i non-passive, drag-n-drop, zarz±dzanie po³±czeniami
i wiele innych mo¿liwo¶ci.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make 

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
README TODO THANKS USERS-GUIDE ChangeLog eplf.txt

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,TODO,THANKS,USERS-GUIDE,ChangeLog,eplf.txt}.gz

%attr(755,root,root) %{_bindir}/gftp

%dir %{_datadir}/gftp
%{_datadir}/gftp/*.xpm
%{_datadir}/gftp/COPYING
%config %{_datadir}/gftp/gftprc
%config %{_datadir}/gftp/bookmarks

%{_datadir}/pixmaps/gftp.png
%{_mandir}/man1/*

%{_applnkdir}/Networking/FTP/gftp.desktop
