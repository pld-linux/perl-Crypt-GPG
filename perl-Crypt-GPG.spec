#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	GPG
Summary:	Crypt::GPG Perl module - an Object Oriented interface to GnuPG
Summary(pl):	Modu³ Perla Crypt::GPG - obiektowo zorientowany interfejs do GnuPG
Name:		perl-Crypt-GPG
Version:	1.42
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Expect >= 1.15
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-TimeDate
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
Modu³ Crypt::GPG daje prawie ca³kowity dostêp do funkcjonalno¶ci GnuPG
poprzez zorientowany obiektowo interfejs. Udostêpnia metody do
szyfrowania, odszyfrowywania, podpisywania, weryfikacji podpisów,
generowania kluczy, eksportowania i importowania kluczy oraz wielu
innych funkcji zwi±zanych z zarz±dzaniem kluczami. Ten modu³ dzia³a
prawie identycznie jak jego kuzyn, Crypt::PGP5. Oba modu³y razem daj±
jednolity interfejs do obs³ugi PGP i GnuPG. Byæ mo¿e te zostan± one
po³±czone w jeden modu³, bêd±cy interfejsem jednocze¶nie do GnuPG i
wszystkich wersji PGP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
# test disabled by default - it calls gpg, creates keyring etc.
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%{perl_sitelib}/Crypt/GPG.pm
%{_mandir}/man3/*
