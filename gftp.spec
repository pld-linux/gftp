Summary:	Multithreaded FTP client for X Window
Summary(pl):	Wielow±tkowy klient FTP dla X Window
Name:		gftp
Version:	2.0.1
Release:	1
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Copyright:	GPL
Source0:	http://www.newwave.net/~masneyb/%{name}-%{version}.tar.gz
Source1:	gftp.desktop
Patch:		gftp-pld.patch
URL:		http://www.newwave.net/~masneyb/
BuildPrereq:	gtk+-devel
BuildPrereq:	glib-devel
BuildPrereq:	XFree86-devel
Buildroot:      /tmp/%{name}-%{version}-root

%define _prefix         /usr/X11R6

%description
gFTP is a multithreaded FTP client for X Window written using Gtk. It
allows to have simultaneous downloads, resuming of interrupted file
transfers, file transfer queues, a very nice connection manager and
many more features.

%description -l pl
gFTP jest wielow±tkowym klientem FTP dla X Window, napisanym przy u¿yciu Gtk.
Pozwala na jednoczesne ¶ci±ganie wielu plików, wznawianie przerwanych 
transferów, kolejkowanie przesy³anych plików, posiada bardzo przyjemnego 
zarz±dcê po³±czeñ i wiele innych mo¿liwo¶ci.

%prep
%setup -q
%patch -p0

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix} \
	--with-x

make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/gftp} \
	$RPM_BUILD_ROOT/etc/X11/applnk/Networking/FTP

make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Networking/FTP

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
* Mon May 17 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [2.0.1-1]
- updated to 2.0.1,
- removed wmconfig file,
- added using more rpm macors.

* Sun May 16 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [2.0.0-1]
- updated to 2.0.0,
- removed gftp-DESTDIR.patch,
- changed gftp.desktop path,
- more BuildPrereq rules,
- package is FHS 2.0 compliant.

* Mon Apr 19 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.13-2]
- recompiled on new rpm.

* Thu Apr  1 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.13-1]
- updated to 1.13,
- added using ./configure in %build,
- removed gftp-opt.patch (we don't need this anymore),
- "make install" with using DESTDIR (gftp-DESTDIR.patch),
- minor changes.

* Mon Mar 29 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.12-4]
- added wmconfig file,
- added gftp-pld.patch,
- fixed Source description,
- changed Group to X11/Applications/Networking,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added "Requires: gtk+ = 1.2.1",
- added pl translation,
- added -q %setup parameter,
- changed PREFIX to /usr/X11R6,
- fixed passing RPM_OPT_FLAGS (gftp-opt.patch),
- simplifications in %install,
- added gzipping documentation,
- added full %defattr description in %files,
- moved %changelog at the end of spec,
- minor changes.

* Tue Feb 16 1999 Michael Fulbright <drmike@redhat.com>
- version 1.12

* Wed Feb 10 1999 Michael Fulbright <drmike@redhat.com>
- first attempt at spec file
