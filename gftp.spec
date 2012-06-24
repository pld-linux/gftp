Summary:	Multithreaded FTP client for X Window
Summary(es):	Cliente FTP multithreaded para el X Windows
Summary(ja):	X Window System �ѥޥ������å� FTP ���饤�����
Summary(pl):	Wielow�tkowy klient FTP dla X Window
Summary(pt_BR):	Cliente FTP multithreaded para o X Window
Summary(ru):	������������ FTP ������ ��� X Window
Summary(uk):	�������������� FTP �̦��� ��� X Window
Name:		gftp
Version:	2.0.14
Release:	3
Epoch:		2
License:	GPL
Group:		X11/Applications/Networking
Source0:	ftp://www.gftp.org/pub/gftp/old-releases/%{name}-%{version}.tar.gz
# Source0-md5:	61e1271af88de20b50a90242a648ab2b
Patch0:		%{name}-pld.patch
Patch1:		%{name}-no_libnsl.patch
Patch2:		%{name}-am_fixes.patch
Patch3:		%{name}-desktop.patch
URL:		http://gftp.seul.org/
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gFTP is a multithreaded FTP client for X Windows written using Gtk. It
features simultaneous downloads, resuming of interrupted file
transfers, file transfer queues, downloading of entire directories,
ftp proxy support, remote directory caching, passive and non-passive
file transfers, drag-n-drop support, bookmarks menu, stop button, and
many more features.

%description -l es
Cliente FTP multithreaded para el X Windows.

%description -l ja
gFTP �� X Window System �ѤΥޥ������å� FTP ���饤����ȤǤ���
gFTP �ϡ�ʣ���ե������Ʊ����������ɤ䡢���Ǥ���ž����
�쥸�塼�ࡢʣ���Υե�����Υ��������ͽ�󡢥ǥ��쥯�ȥꤴ�Ȥ�
��������ɡ� FTP �����ȤΥ֥å��ޡ����� FTP �����ȤΥǥ��쥯�ȥ�
�Υ���å��塢������ȥ�⡼�ȤΥե�����Υѡ��ߥå������ѹ���
�ɥ�å�����ɥɥ�åס����ͥ������ޥ͡����㡢����¾�������
��ǽ����äƤ��ޤ���

%description -l pl
gFTP jest wielow�tkowym klientem FTP dla X Window wykorzystuj�cym
bibliotek� gtk+. Pozwala na jednoczesne �ci�ganie wielu plik�w,
wznawianie przerwanych transfer�w, kolejkowanie przesy�anych plik�w,
�ci�ganie zawarto�ci katalog�w, mo�liwo�� pracy z wykorzystaniem ftp
proxy, �ci�gnie plik�w w trybie passiv i non-passive, drag-n-drop,
zarz�dzanie po��czeniami i wiele innych mo�liwo�ci.

%description -l pt_BR
O gftp � um cliente FTP multithreaded para o X Window escrito usando a
biblioteca gtk. Permite transferir arquivos simult�neamente, continuar
transfer�ncias interrompidas, filas para transfer�ncias de arquivos e
um gerenciador de conex�es muito bom e muitas outras caracter�sticas.

%description -l ru
gFTP - ������������ FTP ������ ��� X Window ��������� � ��������������
GTK. ����� ��� ������������ ������������� �������� ������ ������,
����������� ��������� ������� ������, ������� �� ��������, ��������
����� ���������, ��������� ftp ������, ��� �������� ���������
���������, �������� ������ � �������� � ���������� �������, ���������
"������������" ������ (drag-n-drop), ���� ��������, ������ �������� �
����� �������.

%description -l uk
gFTP � �������������� FTP �̦����� ��� X Window, ��������� �
������������� GTK. ����� ���� ����������� �������Φ ������������
�������� ���̦�, ����������� ���������� ������� ���̦�, ����� ��
��������, ������������ æ��� ������Ǧ�, Ц������� ftp ����Ӧ, ���
�����Ӧ� צ�������� ������Ǧ�, �������� ���̦� � ��������� ��
����������� �������, Ц������� "����������" ���̦� (drag-n-drop), ����
����������, ������ ������� �� ������ ������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO THANKS docs/USERS-GUIDE ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/gftp
%{_datadir}/gftp/*.xpm
%{_datadir}/gftp/COPYING
%config %{_datadir}/gftp/gftprc
%config %{_datadir}/gftp/bookmarks

%{_pixmapsdir}/gftp.png
%{_mandir}/man1/*

%{_applnkdir}/Network/FTP/gftp.desktop
