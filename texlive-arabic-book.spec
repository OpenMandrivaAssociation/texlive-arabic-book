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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/xelatex
%dir %{_datadir}/texmf-dist/tex/xelatex
%dir %{_datadir}/texmf-dist/doc/xelatex/arabic-book
%dir %{_datadir}/texmf-dist/tex/xelatex/arabic-book
%doc %{_datadir}/texmf-dist/doc/xelatex/arabic-book/README.txt
%doc %{_datadir}/texmf-dist/doc/xelatex/arabic-book/arabic-book.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/arabic-book/arabic-book.tex
%doc %{_datadir}/texmf-dist/doc/xelatex/arabic-book/arabic-ref.bib
%doc %{_datadir}/texmf-dist/doc/xelatex/arabic-book/fig1.png
%{_datadir}/texmf-dist/tex/xelatex/arabic-book/arabic-book.cls
