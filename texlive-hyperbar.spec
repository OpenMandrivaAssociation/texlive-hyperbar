%global tl_name hyperbar
%global tl_revision 48147

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Add interactive Barcode fields to PDF forms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hyperbar
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperbar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperbar.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperbar.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends the hyperref functionality for creating interactive
forms to allow adding Barcode form fields supported by some modern PDF
readers. Currently, only pdfTeX is supported.

