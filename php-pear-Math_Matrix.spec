%define		_status		beta
%define		_pearname	Math_Matrix
Summary:	%{_pearname} - class to represent matrices and matrix operations
Summary(pl.UTF-8):	%{_pearname} - klasa do prezentowanie macierzy i operacji na nich
Name:		php-pear-%{_pearname}
Version:	0.8.7
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	15412fb97880ef4a57567fda664a2120
URL:		http://pear.php.net/package/Math_Matrix/
BuildRequires:	php-pear-PEAR >= 1:1.5.6
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Math_Vector >= 0.7.0
Obsoletes:	php-pear-Math_Matrix-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(PHPUnit.*)

%description
Matrices are represented as 2 dimensional arrays of numbers. This
class defines methods for matrix objects, as well as static methods to
read, write and manipulate matrices, including methods to solve
systems of linear equations (with and without iterative error
correction).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Macierze są reprezentowane przez dwuwymiarowe tablice liczb. Ta klasa
definiuje metody dla obiektów macierzy, jak również statyczne metody
do czytania, zapisywania i manipulowania macierzami, włączając w to
metody do rozwiązywania układów równań liniowych (z bądź bez
iteracyjnej korekcji błędów).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/Matrix.php

%{php_pear_dir}/data/%{_pearname}
