Name:		python-pyproject-metadata
Version:	0.11.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pyproject_metadata/pyproject_metadata-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	PEP 621 metadata parsing
URL:		https://pypi.org/project/pyproject-metadata/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%rename python-pyproject_metadata

%description
PEP 621 metadata parsing

%files
%{py_sitedir}/pyproject_metadata
%{py_sitedir}/pyproject_metadata-*.*-info
