%define upstream_name    BerkeleyDB-Manager
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	General purpose L<BerkeleyDB> wrapper
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/BerkeleyDB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(BerkeleyDB)
BuildRequires:	perl(Data::Stream::Bulk)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::TempDir)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(File::NFSLock)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
This object provides a convenience wrapper for the BerkeleyDB manpage

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
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 654223
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 625086
- import perl-BerkeleyDB-Manager

