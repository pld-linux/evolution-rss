Summary:	RSS Reader for Evolution Mail
Summary(pl.UTF-8):	Czytnik kanałów informacyjnych RSS dla Evolution
Name:		evolution-rss
Version:	0.0.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://mips.edu.ms/%{name}-%{version}.tar.gz
# Source0-md5:	138efe707780f3ac4a56867d0a0cdf91
URL:		http://mips.edu.ms/evo/index.php/Evolution_RSS_Reader_Plugin
BuildRequires:	GConf2-devel >= 2.18.0.1
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.10.0
BuildRequires:	gtk+2-devel >= 2:2.10.10
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libgnomeui-devel >= 2.18.1
BuildRequires:	libsoup-devel >= 2.2.100
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	evolution >= 2.10.0
Requires:	gtk+2 >= 2:2.10.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RSS Reader for Evolution Mail

%description -l pl.UTF-8
Czytnik kanałów informacyjnych RSS dla Evolution

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_datadir}/%{name}/glade/rss-ui.glade
%{_libdir}/bonobo/servers/*.server
%attr(755,root,root) %{_libdir}/evolution/*/plugins/*.so
%{_libdir}/evolution/*/plugins/org*
%{_datadir}/evolution/*/images/*.png
