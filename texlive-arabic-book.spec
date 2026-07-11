%global tl_name arabic-book
%global tl_revision 59594

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	An Arabic book class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/arabic-book
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabic-book.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabic-book.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This document class provides both Arabic and English support for
TeX/LaTeX. Input may be in ASCII transliteration or other encodings
(including UTF-8), and output may be Arabic, Hebrew, or any of several
languages that use the Arabic script, as can be specified by the
polyglossia package. The Arabic font is presently available in any
Arabic fonts style. In order to use Amiri font style, the user needs to
install the amiri package. This document class runs with the XeTeX
engine. PDF files generated using this class can be searched, and text
can be copied from them and pasted elsewhere.

