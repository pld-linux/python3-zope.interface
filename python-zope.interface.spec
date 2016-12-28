#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

# NOTE: 'module' should match the python import path, not the egg name
%define 	module	zope.interface
Summary:	Python 'interface' concept implementation
Summary(pl.UTF-8):	Implementacja interfejsów dla języka Python
Name:		python-%{module}
Version:	4.0.3
Release:	2
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz
# Source0-md5:	1ddd308f2c83703accd1696158c300eb
URL:		http://docs.zope.org/zope.interface/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
Requires:	python-zope-base
Provides:	ZopeInterface
Provides:	Zope-Interface
Obsoletes:	ZopeInterface
Obsoletes:	Zope-Interface
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 'interface' concept implementation.

%description -l pl.UTF-8
Implementacja interfejsów (abstrakcyjnych reprezentacji klas) dla
języka Python.

%package -n python3-%{module}
Summary:	Python 'interface' concept implementation
Summary(pl.UTF-8):	Implementacja interfejsów dla języka Python
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-zope-base

%description -n python3-%{module}
Python 'interface' concept implementation.

%description -n python3-%{module} -l pl.UTF-8
Implementacja interfejsów (abstrakcyjnych reprezentacji klas) dla
języka Python.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/*.c

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/zope/interface/*.c
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt
%dir %{py_sitedir}/zope/interface
%{py_sitedir}/zope/interface/*.py[co]
%attr(755,root,root) %{py_sitedir}/zope/interface/_zope_interface_coptimizations.so
%{py_sitedir}/zope/interface/common
%{py_sitedir}/zope/interface/tests
%{py_sitedir}/zope.interface-*.egg-info
%{py_sitedir}/zope.interface-*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.txt
%dir %{py3_sitedir}/zope/interface
%{py3_sitedir}/zope/interface/*.py
%{py3_sitedir}/zope/interface/__pycache__
%attr(755,root,root) %{py3_sitedir}/zope/interface/_zope_interface_coptimizations*.so
%{py3_sitedir}/zope/interface/common
%{py3_sitedir}/zope/interface/tests
%{py3_sitedir}/zope.interface-*.egg-info
%{py3_sitedir}/zope.interface-*-nspkg.pth
%endif
