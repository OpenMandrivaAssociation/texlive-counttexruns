# revision 27576
# category Package
# catalog-ctan /macros/latex/contrib/counttexruns
# catalog-date 2012-08-31 19:14:38 +0200
# catalog-license lppl1.3
# catalog-version 1.00a
Name:		texlive-counttexruns
Version:	1.00a
Release:	6
Summary:	Count compilations of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/counttexruns
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/counttexruns.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/counttexruns.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/counttexruns.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package counts how often a LaTeX document is compiled,
keeping the data in an external file. To print the count, can
use the macro \thecounttexruns.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/counttexruns/counttexruns.sty
%doc %{_texmfdistdir}/doc/latex/counttexruns/README
%doc %{_texmfdistdir}/doc/latex/counttexruns/counttexruns.pdf
#- source
%doc %{_texmfdistdir}/source/latex/counttexruns/counttexruns.dtx
%doc %{_texmfdistdir}/source/latex/counttexruns/counttexruns.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
