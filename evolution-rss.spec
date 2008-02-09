#
# TODO:
# - change default time check - now is 1 min
# - add webkit / xulrunner bcond
#
Summary:	RSS Reader for Evolution Mail
Summary(pl.UTF-8):	Czytnik kanałów informacyjnych RSS dla Evolution
Name:		evolution-rss
Version:	0.0.6
Release:	5
License:	GPL v2
Group:		X11/Applications
Source0:	http://mips.edu.ms/%{name}-%{version}.tar.gz
# Source0-md5:	3c63c1c794ed4ee6171b495e3abd20ac
Patch0:		%{name}-ac.patch
URL:		http://mips.edu.ms/evo/index.php/Evolution_RSS_Reader_Plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-devel >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.12.1
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libsoup-devel >= 2.2.100
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xulrunner-devel
Requires:	evolution >= 2.12.0
Requires:	gtk+2 >= 2:2.10.10
%requires_eq	xulrunner-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# we have strict deps for xulrunner-libs
%define		_noautoreq	libxpcom.so

%description
RSS Reader for Evolution Mail.

%description -l pl.UTF-8
Czytnik kanałów informacyjnych RSS dla Evolution.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_datadir}/evolution/*/glade/*.glade
%{_libdir}/bonobo/servers/*.server
%attr(755,root,root) %{_libdir}/evolution/*/plugins/*.so
%{_libdir}/evolution/*/plugins/org*
%{_datadir}/evolution/*/errors/org*
%{_datadir}/evolution/*/images/*.png
