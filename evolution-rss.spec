#
# Conditional build:
%bcond_with	xulrunner	# without XULRunner render
%bcond_without	webkit		# without WebKit render
#
Summary:	RSS Reader for Evolution Mail
Summary(pl.UTF-8):	Czytnik kanałów informacyjnych RSS dla Evolution
Name:		evolution-rss
Version:	0.2.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://gnome.eu.org/%{name}-%{version}.tar.gz
# Source0-md5:	8d5ba1cce5081dc777e69a83695a7962
URL:		http://gnome.eu.org/evo/index.php/Evolution_RSS_Reader_Plugin
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	evolution-devel >= 2.26.0
BuildRequires:	geoclue-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2:2.14.0
%{?with_webkit:BuildRequires:	gtk-webkit-devel}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.24.0
BuildRequires:	libproxy-devel
BuildRequires:	libsoup-gnome-devel >= 2.30
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.527
%{?with_xulrunner:BuildRequires:	xulrunner-devel >= 1.9-5}
Requires(post,postun):	GConf2
Requires:	evolution >= 2.26.0
Requires:	gtk+2 >= 2:2.14.0
%{?with_xulrunner:%requires_eq	xulrunner-libs}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# we have strict deps for xulrunner-libs
%define		_noautoreq	libxpcom.so

%description
RSS Reader for Evolution Mail.

%description -l pl.UTF-8
Czytnik kanałów informacyjnych RSS dla Evolution.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable xulrunner gecko} \
	%{__with xulrunner gecko libxul} \
	%{__enable_disable webkit}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/evolution/*/plugins/liborg-gnome-evolution-rss.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install evolution-rss.schemas

%preun
%gconf_schema_uninstall evolution-rss.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/evolution-import-rss
%attr(755,root,root) %{_libdir}/evolution/*/plugins/liborg-gnome-evolution-rss.so
#%{_libdir}/bonobo/servers/GNOME_Evolution_RSS_*.server
%{_libdir}/evolution/*/plugins/org-gnome-evolution-rss.eplug
%{_libdir}/evolution/*/plugins/org-gnome-evolution-rss.xml
%{_sysconfdir}/gconf/schemas/evolution-rss.schemas
%{_datadir}/evolution/*/errors/org-gnome-evolution-rss.error
%{_datadir}/evolution/*/ui/*.ui
#%{_datadir}/evolution/*/glade/*.glade
%{_datadir}/evolution/*/images/*.png
