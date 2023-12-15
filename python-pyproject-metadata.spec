Name:		python-pyproject-metadata
Version:	0.7.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pyproject-metadata/pyproject-metadata-%{version}.tar.gz
Summary:	PEP 621 metadata parsing
URL:		https://pypi.org/project/pyproject-metadata/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
PEP 621 metadata parsing

%prep
%autosetup -p1 -n pyproject-metadata-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/pyproject_metadata
%{py_sitedir}/pyproject_metadata-*.*-info
