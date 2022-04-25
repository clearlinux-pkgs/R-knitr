#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-knitr
Version  : 1.38
Release  : 114
URL      : https://cran.r-project.org/src/contrib/knitr_1.38.tar.gz
Source0  : https://cran.r-project.org/src/contrib/knitr_1.38.tar.gz
Summary  : A General-Purpose Package for Dynamic Report Generation in R
Group    : Development/Tools
License  : GPL-2.0
Requires: R-evaluate
Requires: R-highr
Requires: R-stringr
Requires: R-xfun
Requires: R-yaml
BuildRequires : R-evaluate
BuildRequires : R-highr
BuildRequires : R-stringr
BuildRequires : R-xfun
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
Provides a general-purpose tool for dynamic report generation in R using
Literate Programming techniques.

%prep
%setup -q -c -n knitr
cd %{_builddir}/knitr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648233293

%install
export SOURCE_DATE_EPOCH=1648233293
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library knitr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library knitr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library knitr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/knitr/CITATION
/usr/lib64/R/library/knitr/DESCRIPTION
/usr/lib64/R/library/knitr/INDEX
/usr/lib64/R/library/knitr/Meta/Rd.rds
/usr/lib64/R/library/knitr/Meta/demo.rds
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
/usr/lib64/R/library/knitr/demo/gwidgets.R
/usr/lib64/R/library/knitr/demo/notebook.R
/usr/lib64/R/library/knitr/doc/datatables.R
/usr/lib64/R/library/knitr/doc/datatables.Rmd
/usr/lib64/R/library/knitr/doc/datatables.html
/usr/lib64/R/library/knitr/doc/docco-classic.R
/usr/lib64/R/library/knitr/doc/docco-classic.Rmd
/usr/lib64/R/library/knitr/doc/docco-classic.html
/usr/lib64/R/library/knitr/doc/docco-linear.R
/usr/lib64/R/library/knitr/doc/docco-linear.Rmd
/usr/lib64/R/library/knitr/doc/docco-linear.html
/usr/lib64/R/library/knitr/doc/index.html
/usr/lib64/R/library/knitr/doc/knit_expand.R
/usr/lib64/R/library/knitr/doc/knit_expand.Rmd
/usr/lib64/R/library/knitr/doc/knit_expand.html
/usr/lib64/R/library/knitr/doc/knit_print.R
/usr/lib64/R/library/knitr/doc/knit_print.Rmd
/usr/lib64/R/library/knitr/doc/knit_print.html
/usr/lib64/R/library/knitr/doc/knitr-html.R
/usr/lib64/R/library/knitr/doc/knitr-html.Rhtml
/usr/lib64/R/library/knitr/doc/knitr-html.html
/usr/lib64/R/library/knitr/doc/knitr-intro.R
/usr/lib64/R/library/knitr/doc/knitr-intro.Rmd
/usr/lib64/R/library/knitr/doc/knitr-intro.html
/usr/lib64/R/library/knitr/doc/knitr-markdown.R
/usr/lib64/R/library/knitr/doc/knitr-markdown.Rmd
/usr/lib64/R/library/knitr/doc/knitr-markdown.html
/usr/lib64/R/library/knitr/doc/knitr-refcard.Rmd
/usr/lib64/R/library/knitr/doc/knitr-refcard.pdf
/usr/lib64/R/library/knitr/examples/README.md
/usr/lib64/R/library/knitr/examples/Sweavel.sty
/usr/lib64/R/library/knitr/examples/child/knitr-child-a.Rnw
/usr/lib64/R/library/knitr/examples/child/knitr-child-b.Rnw
/usr/lib64/R/library/knitr/examples/child/knitr-child.Rmd
/usr/lib64/R/library/knitr/examples/child/knitr-main.Rmd
/usr/lib64/R/library/knitr/examples/child/knitr-main.Rnw
/usr/lib64/R/library/knitr/examples/child/knitr-parent.Rnw
/usr/lib64/R/library/knitr/examples/child/sub/knitr-child-c.Rnw
/usr/lib64/R/library/knitr/examples/download_count.csv
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
/usr/lib64/R/library/knitr/examples/knitr-manual.bib
/usr/lib64/R/library/knitr/examples/knitr-manual.lyx
/usr/lib64/R/library/knitr/examples/knitr-minimal.Rmd
/usr/lib64/R/library/knitr/examples/knitr-minimal.Rnw
/usr/lib64/R/library/knitr/examples/knitr-minimal.Rrst
/usr/lib64/R/library/knitr/examples/knitr-minimal.brew
/usr/lib64/R/library/knitr/examples/knitr-minimal.lyx
/usr/lib64/R/library/knitr/examples/knitr-packages.bib
/usr/lib64/R/library/knitr/examples/knitr-spin.R
/usr/lib64/R/library/knitr/examples/knitr-spin.Rmd
/usr/lib64/R/library/knitr/examples/knitr-spin.html
/usr/lib64/R/library/knitr/examples/knitr-subfloats.Rnw
/usr/lib64/R/library/knitr/examples/knitr-subfloats.lyx
/usr/lib64/R/library/knitr/examples/knitr-themes.Rnw
/usr/lib64/R/library/knitr/examples/knitr-themes.lyx
/usr/lib64/R/library/knitr/examples/knitr-twocolumn.Rnw
/usr/lib64/R/library/knitr/examples/knitr-twocolumn.lyx
/usr/lib64/R/library/knitr/examples/upload-github.R
/usr/lib64/R/library/knitr/help/AnIndex
/usr/lib64/R/library/knitr/help/aliases.rds
/usr/lib64/R/library/knitr/help/knitr.rdb
/usr/lib64/R/library/knitr/help/knitr.rdx
/usr/lib64/R/library/knitr/help/paths.rds
/usr/lib64/R/library/knitr/html/00Index.html
/usr/lib64/R/library/knitr/html/R.css
/usr/lib64/R/library/knitr/misc/R.css
/usr/lib64/R/library/knitr/misc/Sweavel.sty
/usr/lib64/R/library/knitr/misc/datatables.html
/usr/lib64/R/library/knitr/misc/docco-classic.css
/usr/lib64/R/library/knitr/misc/docco-classic.html
/usr/lib64/R/library/knitr/misc/docco-template.html
/usr/lib64/R/library/knitr/misc/gWidgetsWWW2-knitr.R
/usr/lib64/R/library/knitr/misc/knitr-template.Rhtml
/usr/lib64/R/library/knitr/misc/knitr-template.Rmd
/usr/lib64/R/library/knitr/misc/knitr-template.Rnw
/usr/lib64/R/library/knitr/misc/knitr.css
/usr/lib64/R/library/knitr/misc/knitr.sty
/usr/lib64/R/library/knitr/misc/stitch-test.R
/usr/lib64/R/library/knitr/misc/tikz2pdf.tex
/usr/lib64/R/library/knitr/misc/toggleR.js
/usr/lib64/R/library/knitr/misc/tweak_bib.csv
/usr/lib64/R/library/knitr/misc/vignette.css
/usr/lib64/R/library/knitr/misc/vignette.html
/usr/lib64/R/library/knitr/opencpu/apps/index.html
/usr/lib64/R/library/knitr/shiny/server.R
/usr/lib64/R/library/knitr/shiny/ui.R
/usr/lib64/R/library/knitr/shiny/www/ace-shiny.css
/usr/lib64/R/library/knitr/shiny/www/ace-shiny.js
/usr/lib64/R/library/knitr/tests/run-all.R
/usr/lib64/R/library/knitr/tests/testit/acid.style
/usr/lib64/R/library/knitr/tests/testit/knit-envir.Rmd
/usr/lib64/R/library/knitr/tests/testit/knit-handlers.Rmd
/usr/lib64/R/library/knitr/tests/testit/knit-tikzDevice.Rnw
/usr/lib64/R/library/knitr/tests/testit/test-block.R
/usr/lib64/R/library/knitr/tests/testit/test-cache.R
/usr/lib64/R/library/knitr/tests/testit/test-citation.R
/usr/lib64/R/library/knitr/tests/testit/test-closure.R
/usr/lib64/R/library/knitr/tests/testit/test-envir.R
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
