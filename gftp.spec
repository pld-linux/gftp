Summary:	Multithreaded FTP client for X Window
Summary(pl):	Wielow�tkowy klient FTP dla X Window
Name:		gftp
Version:	2.0.5
Release:	1
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Copyright:	GPL
Source0:	http://gftp.seul.org/%{name}-%{version}.tar.gz
Patch0:		gftp-pld.patch
Patch1:		gftp-desktop.patch
URL:		http://gftp.seul.org/
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
BuildRequires:	XFree86-devel
BuildRequires:	gettext-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6

%description
gFTP is a multithreaded FTP client for X Window written using Gtk. It
allows to have simultaneous downloads, resuming of interrupted file
transfers, file transfer queues, a very nice connection manager and
many more features.

%description -l pl
gFTP jest wielow�tkowym klientem FTP dla X Window, napisanym przy u�yciu Gtk.
Pozwala na jednoczesne �ci�ganie wielu plik�w, wznawianie przerwanych 
transfer�w, kolejkowanie przesy�anych plik�w, posiada bardzo przyjemnego 
zarz�dc� po��cze� i wiele innych mo�liwo�ci.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/applnk/Networking/FTP

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO ChangeLog eplf.txt

install gftp.desktop $RPM_BUILD_ROOT%{_datadir}/applnk/Networking/FTP

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,TODO,ChangeLog,eplf.txt}.gz
%attr(755,root,root) %{_bindir}/gftp

%dir %{_datadir}/gftp
%{_datadir}/gftp/*.xpm
%config %{_datadir}/gftp/gftprc

%{_datadir}/applnk/Networking/FTP/gftp.desktop
