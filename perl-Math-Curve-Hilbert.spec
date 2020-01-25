#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Curve-Hilbert
Summary:	Math::Curve::Hilbert - Hilberts space filling curve
Summary(pl.UTF-8):	Math::Curve::Hilbert - krzywa wypełniająca przestrzeń Hilberta
Name:		perl-Math-Curve-Hilbert
Version:	0.04
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	384cad8ba6759efdf0bbbe987350109f
URL:		http://search.cpan.org/dist/Math-Curve-Hilbert/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Hilbert::Curve module provides some useful functions using
Hilberts Space-filling Curve. This is handy for things like Dithering,
Flattening n-dimensional data, fractals - all kind of things really.

%description -l pl.UTF-8
Moduł Hilbert::Curve udostępnia użyteczne funkcje korzystające z
krzywej wypełniającej przestrzeń Hilberta. Jest przydatna do takich
zastosowań jak dithering, wygładzanie n-wymiarowych danych, fraktale.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Math/Curve
%{perl_vendorlib}/Math/Curve/Hilbert.pm
%{_mandir}/man3/*
