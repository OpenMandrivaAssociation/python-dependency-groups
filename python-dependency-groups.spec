Name:		python-dependency-groups
Version:	1.3.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/d/dependency_groups/dependency_groups-%{version}.tar.gz
Summary:	A tool for resolving PEP 735 Dependency Group data
URL:		https://pypi.org/project/dependency-groups/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
A tool for resolving PEP 735 Dependency Group data

%files
%{_bindir}/dependency-groups
%{_bindir}/lint-dependency-groups
%{_bindir}/pip-install-dependency-groups
%{py_sitedir}/dependency_groups
%{py_sitedir}/dependency_groups-*.*-info
