Name:		texlive-arabic-book
Version:	59594
Release:	2
Summary:	An Arabic book class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arabic-book
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabic-book.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabic-book.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This document class provides both Arabic and English support
for TeX/LaTeX. Input may be in ASCII transliteration or other
encodings (including UTF-8), and output may be Arabic, Hebrew,
or any of several languages that use the Arabic script, as can
be specified by the polyglossia package. The Arabic font is
presently available in any Arabic fonts style. In order to use
Amiri font style, the user needs to install the amiri package.
This document class runs with the XeTeX engine. PDF files
generated using this class can be searched, and text can be
copied from them and pasted elsewhere.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/arabic-book
%doc %{_texmfdistdir}/doc/xelatex/arabic-book

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
