%define upstream_name    BerkeleyDB-Manager
Name:		perl-%{upstream_name}
Version:	0.12
Release:	7

Summary:	General purpose L<BerkeleyDB> wrapper
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/BerkeleyDB-Manager
Source0:	https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/BerkeleyDB-Manager-%{version}.tar.gz

BuildRequires:	make
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
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
This object provides a convenience wrapper for the BerkeleyDB manpage

%prep
%setup -q -n %{upstream_name}-%{version}

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
