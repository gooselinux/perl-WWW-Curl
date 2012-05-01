Name:           perl-WWW-Curl
Version:        4.09
Release:        3%{?dist}
Summary:        Perl extension interface for libcurl
License:        MPLv1.1 or MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/WWW-Curl/
Source0:        http://www.cpan.org/authors/id/S/SZ/SZBALINT/WWW-Curl-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 1:5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Base)
BuildRequires:  libcurl-devel
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
WWW::Curl is a Perl extension interface for libcurl.

%prep
%setup -q -n WWW-Curl-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# These tests require network
%{?!_with_network_tests: rm t/01basic.t }
%{?!_with_network_tests: rm t/02callbacks.t }
%{?!_with_network_tests: rm t/04abort-test.t }
%{?!_with_network_tests: rm t/05progress.t }
%{?!_with_network_tests: rm t/09times.t }
%{?!_with_network_tests: rm t/14duphandle.t }
%{?!_with_network_tests: rm t/15duphandle-callback.t }
%{?!_with_network_tests: rm t/18twinhandles.t }
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/WWW*
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 4.09-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.09-1
- Rebuild for 4.09
* Mon Jun  1 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.07-1
- Rebuild for 4.07
* Sat Apr 18 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.06-1
- Step to 4.06
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Wed Jan 14 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-4
- Licence update
* Wed Jan 14 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-3
- README.Win32 file removed
* Wed Jan 14 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-2
- Timestamp preserved
- changelog format fix
- README.Win32 file removed
* Thu Dec 11 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-1
- Initial build with cpan2spec
