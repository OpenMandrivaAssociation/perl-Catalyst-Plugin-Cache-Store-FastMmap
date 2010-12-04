%define upstream_name    Catalyst-Plugin-Cache-Store-FastMmap
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A thin wrapper for
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Cache::FastMmap)
BuildRequires: perl(Catalyst)
BuildRequires: perl(Catalyst::Plugin::Cache)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Test::Exception)
BuildRequires: perl-Test-use-ok
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


