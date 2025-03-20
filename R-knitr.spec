#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-knitr
Version  : 1.50
Release  : 135
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/knitr_1.50.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/knitr_1.50.tar.gz
Summary  : A General-Purpose Package for Dynamic Report Generation in R
Group    : Development/Tools
License  : GPL-2.0
Requires: R-evaluate
Requires: R-highr
Requires: R-xfun
Requires: R-yaml
BuildRequires : R-evaluate
BuildRequires : R-highr
BuildRequires : R-xfun
BuildRequires : R-yaml
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Provides a general-purpose tool for dynamic report generation in R using
Literate Programming techniques.

%prep
%setup -q -n knitr
pushd ..
cp -a knitr buildavx2
popd
pushd ..
cp -a knitr buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742474952

%install
export SOURCE_DATE_EPOCH=1742474952
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/knitr/CITATION
/usr/lib64/R/library/knitr/DESCRIPTION
/usr/lib64/R/library/knitr/INDEX
/usr/lib64/R/library/knitr/Meta/Rd.rds
/usr/lib64/R/library/knitr/Meta/features.rds
/usr/lib64/R/library/knitr/Meta/hsearch.rds
/usr/lib64/R/library/knitr/Meta/links.rds
/usr/lib64/R/library/knitr/Meta/nsInfo.rds
/usr/lib64/R/library/knitr/Meta/package.rds
/usr/lib64/R/library/knitr/Meta/vignette.rds
/usr/lib64/R/library/knitr/NAMESPACE
/usr/lib64/R/library/knitr/NEWS.Rd
/usr/lib64/R/library/knitr/R/knitr
/usr/lib64/R/library/knitr/R/knitr.rdb
/usr/lib64/R/library/knitr/R/knitr.rdx
/usr/lib64/R/library/knitr/bin/knit
/usr/lib64/R/library/knitr/doc/datatables.R
/usr/lib64/R/library/knitr/doc/datatables.Rmd
/usr/lib64/R/library/knitr/doc/datatables.html
/usr/lib64/R/library/knitr/doc/docco-classic.Rmd
/usr/lib64/R/library/knitr/doc/docco-classic.html
/usr/lib64/R/library/knitr/doc/docco-linear.Rmd
/usr/lib64/R/library/knitr/doc/docco-linear.html
/usr/lib64/R/library/knitr/doc/index.html
/usr/lib64/R/library/knitr/doc/knit_expand.R
/usr/lib64/R/library/knitr/doc/knit_expand.Rmd
/usr/lib64/R/library/knitr/doc/knit_expand.html
/usr/lib64/R/library/knitr/doc/knit_print.Rmd
/usr/lib64/R/library/knitr/doc/knit_print.html
/usr/lib64/R/library/knitr/doc/knitr-html.Rhtml
/usr/lib64/R/library/knitr/doc/knitr-html.html
/usr/lib64/R/library/knitr/doc/knitr-intro.R
/usr/lib64/R/library/knitr/doc/knitr-intro.Rmd
/usr/lib64/R/library/knitr/doc/knitr-intro.html
/usr/lib64/R/library/knitr/doc/knitr-markdown.R
/usr/lib64/R/library/knitr/doc/knitr-markdown.Rmd
/usr/lib64/R/library/knitr/doc/knitr-markdown.html
/usr/lib64/R/library/knitr/doc/knitr-refcard.Rmd
/usr/lib64/R/library/knitr/doc/knitr-refcard.html
/usr/lib64/R/library/knitr/examples/README.md
/usr/lib64/R/library/knitr/examples/child/knitr-child-a.Rnw
/usr/lib64/R/library/knitr/examples/child/knitr-child-b.Rnw
/usr/lib64/R/library/knitr/examples/child/knitr-child.Rmd
/usr/lib64/R/library/knitr/examples/child/knitr-child2.Rmd
/usr/lib64/R/library/knitr/examples/child/knitr-main.Rmd
/usr/lib64/R/library/knitr/examples/child/knitr-main.Rnw
/usr/lib64/R/library/knitr/examples/child/knitr-parent.Rnw
/usr/lib64/R/library/knitr/examples/child/sub/knitr-child-c.Rnw
/usr/lib64/R/library/knitr/examples/knit-all.R
/usr/lib64/R/library/knitr/examples/knitr-beamer.Rnw
/usr/lib64/R/library/knitr/examples/knitr-beamer.lyx
/usr/lib64/R/library/knitr/examples/knitr-graphics.Rnw
/usr/lib64/R/library/knitr/examples/knitr-graphics.lyx
/usr/lib64/R/library/knitr/examples/knitr-input-child.Rnw
/usr/lib64/R/library/knitr/examples/knitr-input.Rnw
/usr/lib64/R/library/knitr/examples/knitr-latex.Rtex
/usr/lib64/R/library/knitr/examples/knitr-listings.Rnw
/usr/lib64/R/library/knitr/examples/knitr-listings.lyx
/usr/lib64/R/library/knitr/examples/knitr-manual.Rnw
/usr/lib64/R/library/knitr/examples/knitr-manual.lyx
/usr/lib64/R/library/knitr/examples/knitr-minimal.Rmd
/usr/lib64/R/library/knitr/examples/knitr-minimal.Rnw
/usr/lib64/R/library/knitr/examples/knitr-minimal.Rrst
/usr/lib64/R/library/knitr/examples/knitr-minimal.brew
/usr/lib64/R/library/knitr/examples/knitr-minimal.lyx
/usr/lib64/R/library/knitr/examples/knitr-spin.R
/usr/lib64/R/library/knitr/examples/knitr-spin.Rmd
/usr/lib64/R/library/knitr/examples/knitr-subfloats.Rnw
/usr/lib64/R/library/knitr/examples/knitr-subfloats.lyx
/usr/lib64/R/library/knitr/examples/knitr-themes.Rnw
/usr/lib64/R/library/knitr/examples/knitr-themes.lyx
/usr/lib64/R/library/knitr/examples/knitr-twocolumn.Rnw
/usr/lib64/R/library/knitr/examples/knitr-twocolumn.lyx
/usr/lib64/R/library/knitr/help/AnIndex
/usr/lib64/R/library/knitr/help/aliases.rds
/usr/lib64/R/library/knitr/help/knitr.rdb
/usr/lib64/R/library/knitr/help/knitr.rdx
/usr/lib64/R/library/knitr/help/paths.rds
/usr/lib64/R/library/knitr/html/00Index.html
/usr/lib64/R/library/knitr/html/R.css
/usr/lib64/R/library/knitr/misc/R.css
/usr/lib64/R/library/knitr/misc/Sweavel.sty
/usr/lib64/R/library/knitr/misc/knitr-template.Rhtml
/usr/lib64/R/library/knitr/misc/knitr-template.Rmd
/usr/lib64/R/library/knitr/misc/knitr-template.Rnw
/usr/lib64/R/library/knitr/misc/knitr.css
/usr/lib64/R/library/knitr/misc/knitr.sty
/usr/lib64/R/library/knitr/misc/stitch-test.R
/usr/lib64/R/library/knitr/misc/tikz2pdf.tex
/usr/lib64/R/library/knitr/misc/toggleR.js
/usr/lib64/R/library/knitr/misc/vignette.css
/usr/lib64/R/library/knitr/misc/vignette.html
/usr/lib64/R/library/knitr/opencpu/apps/index.html
/usr/lib64/R/library/knitr/tests/run-all.R
/usr/lib64/R/library/knitr/tests/testit/acid.style
/usr/lib64/R/library/knitr/tests/testit/knit-envir.Rmd
/usr/lib64/R/library/knitr/tests/testit/knit-handlers.Rmd
/usr/lib64/R/library/knitr/tests/testit/knit-tikzDevice.Rnw
/usr/lib64/R/library/knitr/tests/testit/test-block.R
/usr/lib64/R/library/knitr/tests/testit/test-cache.R
/usr/lib64/R/library/knitr/tests/testit/test-closure.R
/usr/lib64/R/library/knitr/tests/testit/test-envir.R
/usr/lib64/R/library/knitr/tests/testit/test-hooks-latex.R
/usr/lib64/R/library/knitr/tests/testit/test-hooks-md.R
/usr/lib64/R/library/knitr/tests/testit/test-output.R
/usr/lib64/R/library/knitr/tests/testit/test-params.R
/usr/lib64/R/library/knitr/tests/testit/test-parser.R
/usr/lib64/R/library/knitr/tests/testit/test-patterns.R
/usr/lib64/R/library/knitr/tests/testit/test-plot.R
/usr/lib64/R/library/knitr/tests/testit/test-spin.R
/usr/lib64/R/library/knitr/tests/testit/test-sql.R
/usr/lib64/R/library/knitr/tests/testit/test-table.R
/usr/lib64/R/library/knitr/tests/testit/test-tangle.R
/usr/lib64/R/library/knitr/tests/testit/test-templates.R
/usr/lib64/R/library/knitr/tests/testit/test-themes.R
/usr/lib64/R/library/knitr/tests/testit/test-utils.R
/usr/lib64/R/library/knitr/themes/acid.css
/usr/lib64/R/library/knitr/themes/aiseered.css
/usr/lib64/R/library/knitr/themes/andes.css
/usr/lib64/R/library/knitr/themes/anotherdark.css
/usr/lib64/R/library/knitr/themes/autumn.css
/usr/lib64/R/library/knitr/themes/baycomb.css
/usr/lib64/R/library/knitr/themes/bclear.css
/usr/lib64/R/library/knitr/themes/biogoo.css
/usr/lib64/R/library/knitr/themes/bipolar.css
/usr/lib64/R/library/knitr/themes/blacknblue.css
/usr/lib64/R/library/knitr/themes/bluegreen.css
/usr/lib64/R/library/knitr/themes/breeze.css
/usr/lib64/R/library/knitr/themes/bright.css
/usr/lib64/R/library/knitr/themes/camo.css
/usr/lib64/R/library/knitr/themes/candy.css
/usr/lib64/R/library/knitr/themes/clarity.css
/usr/lib64/R/library/knitr/themes/dante.css
/usr/lib64/R/library/knitr/themes/darkblue.css
/usr/lib64/R/library/knitr/themes/darkbone.css
/usr/lib64/R/library/knitr/themes/darkness.css
/usr/lib64/R/library/knitr/themes/darkslategray.css
/usr/lib64/R/library/knitr/themes/darkspectrum.css
/usr/lib64/R/library/knitr/themes/default.css
/usr/lib64/R/library/knitr/themes/denim.css
/usr/lib64/R/library/knitr/themes/dusk.css
/usr/lib64/R/library/knitr/themes/earendel.css
/usr/lib64/R/library/knitr/themes/easter.css
/usr/lib64/R/library/knitr/themes/edit-anjuta.css
/usr/lib64/R/library/knitr/themes/edit-eclipse.css
/usr/lib64/R/library/knitr/themes/edit-emacs.css
/usr/lib64/R/library/knitr/themes/edit-flashdevelop.css
/usr/lib64/R/library/knitr/themes/edit-gedit.css
/usr/lib64/R/library/knitr/themes/edit-jedit.css
/usr/lib64/R/library/knitr/themes/edit-kwrite.css
/usr/lib64/R/library/knitr/themes/edit-matlab.css
/usr/lib64/R/library/knitr/themes/edit-msvs2008.css
/usr/lib64/R/library/knitr/themes/edit-nedit.css
/usr/lib64/R/library/knitr/themes/edit-vim-dark.css
/usr/lib64/R/library/knitr/themes/edit-vim.css
/usr/lib64/R/library/knitr/themes/edit-xcode.css
/usr/lib64/R/library/knitr/themes/ekvoli.css
/usr/lib64/R/library/knitr/themes/fine_blue.css
/usr/lib64/R/library/knitr/themes/freya.css
/usr/lib64/R/library/knitr/themes/fruit.css
/usr/lib64/R/library/knitr/themes/golden.css
/usr/lib64/R/library/knitr/themes/greenlcd.css
/usr/lib64/R/library/knitr/themes/greyscale0.css
/usr/lib64/R/library/knitr/themes/greyscale1.css
/usr/lib64/R/library/knitr/themes/greyscale2.css
/usr/lib64/R/library/knitr/themes/kellys.css
/usr/lib64/R/library/knitr/themes/leo.css
/usr/lib64/R/library/knitr/themes/lucretia.css
/usr/lib64/R/library/knitr/themes/manxome.css
/usr/lib64/R/library/knitr/themes/maroloccio.css
/usr/lib64/R/library/knitr/themes/matrix.css
/usr/lib64/R/library/knitr/themes/moe.css
/usr/lib64/R/library/knitr/themes/molokai.css
/usr/lib64/R/library/knitr/themes/moria.css
/usr/lib64/R/library/knitr/themes/navajo-night.css
/usr/lib64/R/library/knitr/themes/navy.css
/usr/lib64/R/library/knitr/themes/neon.css
/usr/lib64/R/library/knitr/themes/night.css
/usr/lib64/R/library/knitr/themes/nightshimmer.css
/usr/lib64/R/library/knitr/themes/nuvola.css
/usr/lib64/R/library/knitr/themes/olive.css
/usr/lib64/R/library/knitr/themes/orion.css
/usr/lib64/R/library/knitr/themes/oxygenated.css
/usr/lib64/R/library/knitr/themes/pablo.css
/usr/lib64/R/library/knitr/themes/peaksea.css
/usr/lib64/R/library/knitr/themes/print.css
/usr/lib64/R/library/knitr/themes/rand01.css
/usr/lib64/R/library/knitr/themes/rdark.css
/usr/lib64/R/library/knitr/themes/relaxedgreen.css
/usr/lib64/R/library/knitr/themes/rootwater.css
/usr/lib64/R/library/knitr/themes/seashell.css
/usr/lib64/R/library/knitr/themes/solarized-dark.css
/usr/lib64/R/library/knitr/themes/solarized-light.css
/usr/lib64/R/library/knitr/themes/tabula.css
/usr/lib64/R/library/knitr/themes/tcsoft.css
/usr/lib64/R/library/knitr/themes/vampire.css
/usr/lib64/R/library/knitr/themes/whitengrey.css
/usr/lib64/R/library/knitr/themes/xoria256.css
/usr/lib64/R/library/knitr/themes/zellner.css
/usr/lib64/R/library/knitr/themes/zenburn.css
/usr/lib64/R/library/knitr/themes/zmrok.css
