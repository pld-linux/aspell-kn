Summary:	Kannada dictionary for aspell
Summary(pl.UTF-8):	Słownik języka kannada dla aspella
Name:		aspell-kn
Version:	0.01
%define	subv	1
Release:	3
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/kn/aspell6-kn-%{version}-%{subv}.tar.bz2
# Source0-md5:	0359676017bf18a761b02346d3cc3253
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kannada dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik (lista słów) języka kannada dla aspella.

%prep
%setup -q -n aspell6-kn-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_prefix}/lib/aspell/kannada.alias
%{_prefix}/lib/aspell/kn.multi
%{_prefix}/lib/aspell/kn.rws
%{_datadir}/aspell/kn.dat
%{_datadir}/aspell/u-knda.cmap
%{_datadir}/aspell/u-knda.cset
