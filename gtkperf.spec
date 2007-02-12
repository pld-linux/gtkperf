Summary:	GTK+ performance tester
Summary(pl.UTF-8):   Tester wydajności GTK+
Name:		gtkperf
Version:	0.40
Release:	1
Epoch:		0
License:	GPL v.2
Group:		Applications
Source0:	http://dl.sourceforge.net/gtkperf/%{name}_%{version}.tar.gz
# Source0-md5:	4331dde4bb83865e15482885fcb0cc53
Patch0:		%{name}-desktop.patch
URL:		http://gtkperf.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkPerf is an application designed to test GTK+ performance. The point
is to create common testing platform to run predefined GTK+ widgets
and this way define the speed of device/platform.

%description -l pl.UTF-8
GtkPerf jest programem zaprojektowanym do testowania wydajności GTK+.
Celem jego jest stworzenie ogólnej platformy testowej i uruchamiania
na niej widgetów GTK+ co umożliwiałoby określenie prędkości
urządzenia/platformy.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install data/gtkperf.desktop $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_pixmapsdir}/duck.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/gtkperf.png

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
