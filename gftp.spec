Summary:	Multithreaded FTP client for X Window
Summary(pl):	Wielow±tkowy klient FTP dla X Window
Name:		gftp
Version:	1.13	
Release:	2
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Copyright:	GPL
Source0:	http://www.newwave.net/~masneyb/%{name}-%{version}.tar.gz
Source1:	gftp.desktop
Source2:	gftp.wmconfig
Patch0:		gftp-DESTDIR.patch
Patch1:		gftp-pld.patch
URL:		http://www.newwave.net/~masneyb/
BuildPrereq:	gtk+-devel
%requires_pkg	gtk+
Buildroot:      /tmp/%{name}-%{version}-root

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
%setup  -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--prefix=/usr/X11R6 \
	--with-x

make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,share/{gftp,gnome/apps/Internet}} \
	$RPM_BUILD_ROOT/etc/X11/wmconfig

make install DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/gnome/apps/Internet
install %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/wmconfig/gftp

gzip -9nf README TODO CHANGELOG eplf.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,CHANGELOG,eplf.txt}.gz

%attr(755,root,root) /usr/X11R6/bin/gftp
/usr/X11R6/share/gnome/apps/Internet/gftp.desktop
%dir /usr/X11R6/share/gftp
/usr/X11R6/share/gftp/gftprc
/usr/X11R6/share/gftp/*.xpm

%config(missingok) /etc/X11/wmconfig/gftp

%changelog
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
