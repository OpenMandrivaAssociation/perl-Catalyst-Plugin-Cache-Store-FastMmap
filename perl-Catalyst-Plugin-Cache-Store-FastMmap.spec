%define upstream_name    Catalyst-Plugin-Cache-Store-FastMmap
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	A thin wrapper for
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cache::FastMmap)
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Catalyst::Plugin::Cache)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl-Test-use-ok
BuildArch:	noarch

%description
This store plugin is a bit of a wrapper for the Cache::FastMmap manpage.

While you could normally just configure with

    backend => {
        class => "Cache::FastMmap",
        share_file => ...,
    }

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.20.0-3mdv2011.0
+ Revision: 654257
- rebuild for updated spec-helper

* Sat Dec 04 2010 Shlomi Fish <shlomif@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 609251
- Add missing build dependencies
- import perl-Catalyst-Plugin-Cache-Store-FastMmap

