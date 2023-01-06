Name:           libecap
Version:        1.0.1
Release:        6
Summary:        an loadable eCAP adapter for Squid HTTP-Proxy
License:        BSD
URL:            http://www.e-cap.org/
Source0:        http://www.e-cap.org/archive/%{name}-%{version}.tar.gz

Source1:        autoconf.h
BuildRequires:  gcc gcc-c++
Patch0:         0001-update-config.guess-and-config.sub-file.patch

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
%setup -q
%ifarch loongarch64
%patch0 -p1
%endif

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
* Fri Jan 6 2023 doupengda <doupengda@loongson.cn> 1.0.1-6
- update config.guess and config.sub
- fix SOURCE1 file autoconf.h '__loongarch64__' to '__loongarch64'

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 1.0.1-5
- DESC: delete -Sgit from %autosetup, and delete BuildRequires git

* Wed Aug 28 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0.1-4
- Package init
