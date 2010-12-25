%define upstream_name    BerkeleyDB-Manager
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    General purpose L<BerkeleyDB> wrapper
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/BerkeleyDB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(BerkeleyDB)
BuildRequires: perl(Data::Stream::Bulk)
BuildRequires: perl(Moose)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::TempDir)
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This object provides a convenience wrapper for the BerkeleyDB manpage

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


