%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Matrix
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - class to represent matrices and matrix operations
Summary(pl):	%{_pearname} - klasa do prezentowanie macierzy i operacji na nich
Name:		php-pear-%{_pearname}
Version:	0.8.5
Release:	2.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6ffaa481a6ae12d0b9aed9206d904a3c
URL:		http://pear.php.net/package/Math_Matrix/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matrices are represented as 2 dimensional arrays of numbers.
This class defines methods for matrix objects, as well as static
methods to read, write and manipulate matrices, including methods to
solve systems of linear equations (with and without iterative error
correction).

In PEAR status of this package is: %{_status}.

%description -l pl
Macierze s± reprezentowane przez dwuwymiarowe tablice liczb. Ta klasa
definiuje metody dla obiektów macierzy, jak równie¿ statyczne metody do
czytania, zapisywania i manipulowania macierzami, w³±czaj±c w to metody
do rozwi±zywania uk³adów równañ liniowych (z b±d¼ bez iteracyjnej
korekcji b³êdów).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/tests/*,tests/%{_pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
