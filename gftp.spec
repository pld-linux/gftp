Summary:	Multithreaded FTP client for X Window
Summary(pl):	Wielow�tkowy klient FTP dla X Window
Name:		gftp
Version:	2.0.3
Release:	1
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Copyright:	GPL
Source0:	http://www.newwave.net/~masneyb/%{name}-%{version}.tar.gz
Patch0:		gftp-pld.patch
Patch1:		gftp-desktop.patch
Patch2:		gftp-DESTDIR.patch
URL:		http://www.newwave.net/~masneyb/
BuildPrereq:	gtk+-devel
BuildPrereq:	glib-devel
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

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
%patch1 -p0
%patch2 -p0

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/gftp} \
	$RPM_BUILD_ROOT/etc/X11/applnk/Networking/FTP

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO CHANGELOG eplf.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,CHANGELOG,eplf.txt}.gz
%attr(755,root,root) %{_bindir}/gftp

%dir %{_datadir}/gftp
%{_datadir}/gftp/*.xpm
%config %{_datadir}/gftp/gftprc

/etc/X11/applnk/Networking/FTP/gftp.desktop

%changelog
* Sat Jun 26 1999 Piotr Czerwi�ski <pius@pld.org.pl> 
  [2.0.2-1]
- updated to 2.0.2.

* Fri May 21 1999 Piotr Czerwi�ski <pius@pld.org.pl> 
  [2.0.1-1]
- package is FHS 2.0 compliant,
- spec file rewritten for PLD use,
- based on spec written by Michael Fulbright <drmike@redhat.com>.
