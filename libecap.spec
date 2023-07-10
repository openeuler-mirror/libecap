Name:           libecap
Version:        1.0.1
Release:        5
Summary:        an loadable eCAP adapter for Squid HTTP-Proxy
License:        BSD
URL:            http://www.e-cap.org/
Source0:        http://www.e-cap.org/archive/%{name}-%{version}.tar.gz

Source1:        autoconf.h
BuildRequires:  git gcc gcc-c++

%description
eCAP is a software interface that allows a network application,
such as an HTTP proxy or an ICAP server, to outsource content
analysis and adaptation to a loadable module.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
Development files for %{name}

%package        help
Summary:        Help files for %{name}
BuildArch:	noarch
%description    help
Help files for %{name}

%prep
%autosetup -n %{name}-%{version} -p1 -Sgit

%build
%configure
%make_build

%install
%make_install
pushd %{buildroot}%{_includedir}/%{name}/common
mv autoconf.h autoconf-%{_arch}.h
install -m0644 %{SOURCE1} .
popd
%delete_la_and_a

%check
make check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc CREDITS LICENSE NOTICE
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/%{name}.so
%{_includedir}/%{name}*
%{_libdir}/pkgconfig/%{name}.pc

%files help
%defattr(-,root,root)
%doc README

%changelog
* Mon Jul 03 2023 wangyangdahai <wangyang22@iscas.ac.cn> - 1.0.1-5
- fix riscv64 arch autoconf.h include path

* Wed Aug 28 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0.1-4
- Package init
