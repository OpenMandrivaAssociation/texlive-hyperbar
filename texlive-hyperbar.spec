Name:		texlive-hyperbar
Version:	48147
Release:	2
Summary:	Add interactive Barcode fields to PDF forms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hyperbar
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperbar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperbar.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperbar.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends the hyperref functionality for creating
interactive forms to allow adding Barcode form fields supported
by some modern PDF readers. Currently, only pdfTeX is
supported.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hyperbar
%{_texmfdistdir}/tex/latex/hyperbar
%doc %{_texmfdistdir}/doc/latex/hyperbar

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
