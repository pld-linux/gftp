Summary:	Multithreaded FTP client for X Window
Summary(es):	Cliente FTP multithreaded para el X Window
Summary(ja):	X Window System 用マルチスレッド FTP クライアント
Summary(pl):	Wielow�tkowy klient FTP dla X Window
Summary(pt_BR):	Cliente FTP multithreaded para o X Window
Summary(ru):	輓惑藁不砺拱 FTP 北錨淋 通� X Window
Summary(uk):	眩覗塹良塰�徂� FTP 北Δ淋 通� X Window
Name:		gftp
Version:	2.0.16
Release:	5
Epoch:		2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://gftp.seul.org/%{name}-%{version}.tar.gz
# Source0-md5:	94069bfbfdebd5f00eb881fe9440534b
Patch0:		%{name}-pld.patch
Patch1:		%{name}-no_libnsl.patch
Patch2:		%{name}-configure_in.patch
Patch3:		%{name}-desktop.patch
Patch4:		%{name}-sizeof-off_t.patch
Patch5:		%{name}-locale_names.patch
URL:		http://gftp.seul.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gFTP is a multithreaded FTP client for X Window written using GTK+. It
features simultaneous downloads, resuming of interrupted file
transfers, file transfer queues, downloading of entire directories,
FTP proxy support, remote directory caching, passive and non-passive
file transfers, drag-n-drop support, bookmarks menu, stop button, and
many more features.

%description -l es
Cliente FTP multithreaded para el X Window.

%description -l ja
gFTP は X Window System 用のマルチスレッド FTP クライアントです。
gFTP は、複数ファイルの同時ダウンロードや、中断した転送の
レジューム、複数のファイルのダウンロード予約、ディレクトリごとの
ダウンロード、 FTP サイトのブックマーク、 FTP サイトのディレクトリ
のキャッシュ、ローカルとリモートのファイルのパーミッションの変更、
ドラッグアンドドロップ、コネクションマネージャ、その他いろいろな
機能を持っています。

%description -l pl
gFTP jest wielow�tkowym klientem FTP dla X Window wykorzystuj�cym
bibliotek� GTK+. Pozwala na jednoczesne �ci�ganie wielu plik�w,
wznawianie przerwanych transfer�w, kolejkowanie przesy�anych plik�w,
�ci�ganie zawarto�ci katalog�w, mo�liwo倶 pracy z wykorzystaniem FTP
proxy, �ci�ganie plik�w w trybie pasywnym i nie-pasywnym, drag-n-drop,
zarz�dzanie po咳czeniami i wiele innych mo�liwo�ci.

%description -l pt_BR
O gftp � um cliente FTP multithreaded para o X Window escrito usando a
biblioteca GTK+. Permite transferir arquivos simult�neamente, continuar
transfer�ncias interrompidas, filas para transfer�ncias de arquivos e
um gerenciador de conex�es muito bom e muitas outras caracter�sticas.

%description -l ru
gFTP - 洋惑藁不砺拱 FTP 北錨淋 通� X Window 料佗啻隣� � 瓶佻蒙斛彖良斗
GTK. 麭田� 吐� 從斃�嵶腕堙� 歪力徠斗杜料� 攸拝孳冒 洋惑蛭 徳別��,
侑歪鰐崚良� 侑賭彖隣� 佚凖珍� 徳別��, �淌凖追 料 佚凖珍渾, 攸拝孳冒
壇儲� 冒堊模馬�, 佻陳賭嵋� ftp 侑亘喇, 謀� 瀕津睦�� 嫩遡杜隣�
冒堊模馬�, 佚凖珍涸 徳別�� � 仭喇徇詫 � 療仭喇徇詫 凖嵒輿�, 佻陳賭嵋�
"怠睦敏�彖良�" 徳別�� (drag-n-drop), 妖寮 攸北祖亘, 卜椀冒 腕堊力彖 �
洋惑� 漬嫻惑�.

%description -l uk
gFTP � 汰覗塹良塰�徂� FTP 北Δ淋詫 通� X Window, 料佗啻良� �
徂墨夘嘖僧倫� GTK. 鹽凖� 箆馬 溶嵬夫腕堙� 歪力涸嗄� 攸彖淋爽杜倫
汰覗墮枠 徳別ψ, 侑歪�忖杜倫 佚凖叟僧蛭 佚凖珍� 徳別ψ, 淌卩� 料
佚凖珍渾, 攸彖淋爽杜倫 脱棉� 冒堊模忍�, 丶辻夘曜� ftp 侑亘哘, 謀�
ξ津睦ψ 廢陳遡杜蛭 冒堊模忍�, 佚凖珍涸 徳別ψ � 仭喇徇詫� 堊
療仭喇徇詫� 凖嵒輿�, 丶辻夘曜� "怠睦孥僧倫" 徳別ψ (drag-n-drop), 妖寮
攸北祖瀕亘, 卜椀冒 旁佗遼� 堊 汰覗塹 ξ柤馬.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

mv -f po/{no,nb}.po

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
	Utilitiesdir=%{_desktopdir} \
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
%{_desktopdir}/gftp.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/gftp.png
