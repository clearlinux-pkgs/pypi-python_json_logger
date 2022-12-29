#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-python_json_logger
Version  : 2.0.4
Release  : 1
URL      : https://files.pythonhosted.org/packages/0a/c9/3d58b02da0966cd3067ebf99f454bfa01b18d83cfa69b5fb09ddccf94066/python-json-logger-2.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/0a/c9/3d58b02da0966cd3067ebf99f454bfa01b18d83cfa69b5fb09ddccf94066/python-json-logger-2.0.4.tar.gz
Summary  : A python library adding a json log formatter
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-python_json_logger-license = %{version}-%{release}
Requires: pypi-python_json_logger-python = %{version}-%{release}
Requires: pypi-python_json_logger-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![Build Status](https://github.com/madzak/python-json-logger/actions/workflows/build.yml/badge.svg)
[![License](https://img.shields.io/pypi/l/python-json-logger.svg)](https://pypi.python.org/pypi/python-json-logger/)
[![Version](https://img.shields.io/pypi/v/python-json-logger.svg)](https://pypi.python.org/pypi/python-json-logger/)

%package license
Summary: license components for the pypi-python_json_logger package.
Group: Default

%description license
license components for the pypi-python_json_logger package.


%package python
Summary: python components for the pypi-python_json_logger package.
Group: Default
Requires: pypi-python_json_logger-python3 = %{version}-%{release}

%description python
python components for the pypi-python_json_logger package.


%package python3
Summary: python3 components for the pypi-python_json_logger package.
Group: Default
Requires: python3-core
Provides: pypi(python_json_logger)

%description python3
python3 components for the pypi-python_json_logger package.


%prep
%setup -q -n python-json-logger-2.0.4
cd %{_builddir}/python-json-logger-2.0.4
pushd ..
cp -a python-json-logger-2.0.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672328158
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-python_json_logger
cp %{_builddir}/python-json-logger-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-python_json_logger/00c3c985f3bea9e6aaa6d93e36f5cfb0213a8d27 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-python_json_logger/00c3c985f3bea9e6aaa6d93e36f5cfb0213a8d27

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
