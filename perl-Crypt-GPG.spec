#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	GPG
Summary:	Crypt::GPG Perl module - an object oriented interface to GnuPG
Summary(pl):	Modu� Perla Crypt::GPG - obiektowo zorientowany interfejs do GnuPG
Name:		perl-Crypt-GPG
Version:	1.42
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	917b6d649887c179c39da665a1c7955f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Expect >= 1.15
BuildRequires:	perl-TimeDate
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Crypt::GPG module provides near complete access to GnuPG
functionality through an object oriented interface. It provides
methods for encryption, decryption, signing, signature verification,
key generation, key export and import, and most other key management
functions. This module works almost identically to its cousin,
Crypt::PGP5. The two modules together provide a uniform interface to
deal with both PGP and GnuPG. Eventually, these modules will be folded
into a single module which will interface with GnuPG as well as all
versions of PGP.

%description -l pl
Modu� Crypt::GPG daje prawie ca�kowity dost�p do funkcjonalno�ci GnuPG
poprzez zorientowany obiektowo interfejs. Udost�pnia metody do
szyfrowania, odszyfrowywania, podpisywania, weryfikacji podpis�w,
generowania kluczy, eksportowania i importowania kluczy oraz wielu
innych funkcji zwi�zanych z zarz�dzaniem kluczami. Ten modu� dzia�a
prawie identycznie jak jego kuzyn, Crypt::PGP5. Oba modu�y razem daj�
jednolity interfejs do obs�ugi PGP i GnuPG. By� mo�e te zostan� one
po��czone w jeden modu�, b�d�cy interfejsem jednocze�nie do GnuPG i
wszystkich wersji PGP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
# test disabled by default - it calls gpg, creates keyring etc.
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%{perl_vendorlib}/Crypt/GPG.pm
%{_mandir}/man3/*
