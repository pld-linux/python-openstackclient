#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	OpenStack Command-line Client
Name:		python-openstackclient
Version:	3.12.0
Release:	5
License:	Apache
Group:		Libraries/Python
Source0:	http://tarballs.openstack.org/python-openstackclient/%{name}-%{version}.tar.gz
# Source0-md5:	09020f1e10d8b6afe0715c17b389b3c0
URL:		https://docs.openstack.org/python-openstackclient/latest/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-babel >= 2.3.4
BuildRequires:	python-cinderclient >= 3.0.0
BuildRequires:	python-cliff >= 2.8.0
BuildRequires:	python-glanceclient >= 2.7.0
BuildRequires:	python-keystoneauth1 >= 3.0.1
BuildRequires:	python-keystoneclient >= 3.8.0
BuildRequires:	python-novaclient >= 9.0.0
BuildRequires:	python-openstacksdk >= 0.9.17
BuildRequires:	python-osc-lib >= 1.7.0
BuildRequires:	python-oslo.i18n >= 2.10
BuildRequires:	python-oslo.utils >= 3.20.0
BuildRequires:	python-six >= 1.9.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python-six >= 1.9.0
BuildRequires:	python3-babel >= 2.3.4
BuildRequires:	python3-cinderclient >= 3.0.0
BuildRequires:	python3-cliff >= 2.8.0
BuildRequires:	python3-glanceclient >= 2.7.0
BuildRequires:	python3-keystoneauth1 >= 3.0.1
BuildRequires:	python3-keystoneclient >= 3.8.0
BuildRequires:	python3-novaclient >= 9.0.0
BuildRequires:	python3-openstacksdk >= 0.9.17
BuildRequires:	python3-osc-lib >= 1.7.0
BuildRequires:	python3-oslo.i18n >= 2.10
BuildRequires:	python3-oslo.utils >= 3.20.0
BuildRequires:	python3-six >= 1.9.0
%endif
%endif
Requires:	python-babel >= 2.3.4
Requires:	python-cinderclient >= 3.0.0
Requires:	python-cliff >= 2.8.0
Requires:	python-glanceclient >= 2.7.0
Requires:	python-keystoneauth1 >= 3.0.1
Requires:	python-keystoneclient >= 3.8.0
Requires:	python-novaclient >= 9.0.0
Requires:	python-openstacksdk >= 0.9.17
Requires:	python-osc-lib >= 1.7.0
Requires:	python-oslo.i18n >= 2.10
Requires:	python-oslo.utils >= 3.20.0
Requires:	python-six >= 1.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenStack Command-line Client.

This package contains the Python modules, install 'openstackclient'
for the actual tool.

%package -n python3-openstackclient
Summary:	OpenStack Command-line Client
Group:		Libraries/Python
Requires:	python3-babel >= 2.3.4
Requires:	python3-cinderclient >= 3.0.0
Requires:	python3-cliff >= 2.8.0
Requires:	python3-glanceclient >= 2.7.0
Requires:	python3-keystoneauth1 >= 3.0.1
Requires:	python3-keystoneclient >= 3.8.0
Requires:	python3-novaclient >= 9.0.0
Requires:	python3-openstacksdk >= 0.9.17
Requires:	python3-osc-lib >= 1.7.0
Requires:	python3-oslo.i18n >= 2.10
Requires:	python3-oslo.utils >= 3.20.0
Requires:	python3-six >= 1.9.0

%description -n python3-openstackclient
OpenStack Command-line Client.

This package contains the Python modules, install 'openstackclient'
for the actual tool.

%package -n openstackclient
Summary:	OpenStack Command-line Client
Group:		Applications
%if %{with python3}
Requires:	python3-openstackclient = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description -n openstackclient
OpenStack Command-line Client.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/openstackclient
%{py_sitescriptdir}/python_openstackclient-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-openstackclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/openstackclient
%{py3_sitescriptdir}/python_openstackclient-%{version}-py*.egg-info
%endif

%files -n openstackclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/*
