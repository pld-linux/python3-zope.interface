#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (fail with package already installed?)

%define		module	zope.interface
Summary:	Python 'interface' concept implementation
Summary(pl.UTF-8):	Implementacja interfejsów dla języka Python
Name:		python3-%{module}
Version:	7.2
Release:	1
License:	ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zope.interface/
Source0:	https://files.pythonhosted.org/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz
# Source0-md5:	583dac724d227b3ee2d4d4a940425961
URL:		https://zopeinterface.readthedocs.io/
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-coverage >= 5.0.3
BuildRequires:	python3-zope.event
BuildRequires:	python3-zope.testing
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-furo
BuildRequires:	python3-repoze.sphinx.autointerface
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.8
Requires:	python3-zope-base
Provides:	ZopeInterface
Provides:	Zope-Interface
Obsoletes:	ZopeInterface < 3.4.0
Obsoletes:	Zope-Interface < 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 'interface' concept implementation.

%description -l pl.UTF-8
Implementacja interfejsów (abstrakcyjnych reprezentacji klas) dla
języka Python.

%package apidocs
Summary:	API documentation for Python zope.interface module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona zope.interface
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python zope.interface module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona zope.interface.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m unittest discover -s src
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/zope/interface/*.c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt README.rst
%dir %{py3_sitedir}/zope/interface
%{py3_sitedir}/zope/interface/*.py
%{py3_sitedir}/zope/interface/__pycache__
%attr(755,root,root) %{py3_sitedir}/zope/interface/_zope_interface_coptimizations*.so
%{py3_sitedir}/zope/interface/common
%{py3_sitedir}/zope/interface/tests
%{py3_sitedir}/zope.interface-%{version}-py*.egg-info
%{py3_sitedir}/zope.interface-%{version}-py*-nspkg.pth

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,api,*.html,*.js}
%endif
