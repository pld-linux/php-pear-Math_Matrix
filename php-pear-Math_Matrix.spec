%include	/usr/lib/rpm/macros.php
%define         _class          Math
%define         _subclass       Matrix
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Class to represent matrices and matrix operations
Summary(pl):	%{_pearname} - Klasa do prezentowanie macierzy i operacji na nich
Name:		php-pear-%{_pearname}
Version:	0.8.5
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6ffaa481a6ae12d0b9aed9206d904a3c
URL:		http://pear.php.net/package/Math_Matrix/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matrices are represented as 2 dimensional arrays of numbers.
This class defines methods for matrix objects, as well as static
methods to read, write and manipulate matrices, including methods to
solve systems of linear equations (with and without iterative error
correction).

This class has in PEAR status: %{_status}.

%description -l pl
Macierze s± reprezentowane przez dwuwymiarowe tablice liczb. Ta klasa
definiuje metody dla obiektów macierzy, jak równie¿ statyczne metody do
czytania, zapisywania i manipulowania macierzami, w³±czaj±c w to metody
do rozwi±zywania systemów równañ liniowych (z b±d¼ bez iteracyjnej
korekcji b³êdów).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs,tests}
%{php_pear_dir}/%{_class}/*.php
