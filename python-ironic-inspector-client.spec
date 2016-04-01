%global pypi_name python-ironic-inspector-client


%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-ironic-inspector-client
Version:        1.5.0
Release:        1%{?dist}
Summary:        Python client and CLI tool for Ironic Inspector

License:        ASL 2.0
URL:            https://launchpad.net/python-ironic-inspector-client
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}%{?milestone}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools

Requires:  python-cliff
Requires:  python-oslo-i18n
Requires:  python-oslo-utils
Requires:  python-openstackclient
Requires:  python-requests
Requires:  python-six

Obsoletes: python-ironic-discoverd < 1.1.0-3
Provides: python-ironic-discoverd = %{upstream_version}

%description
Ironic Inspector is an auxiliary service for discovering hardware properties
for a node managed by OpenStack Ironic. Hardware introspection or hardware
properties discovery is a process of getting hardware parameters required for
scheduling from a bare metal node, given it’s power management credentials
(e.g. IPMI address, user name and password).

This package contains Python client and command line tool for Ironic Inspector.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python2_sitelib}/ironic_inspector_client*
%{python2_sitelib}/python_ironic_inspector_client*egg-info

%changelog
* Fri Apr  1 2016 RDO <rdo-list@redhat.com> 1.5.0-1
- RC1 Rebuild for Mitaka RC1 
