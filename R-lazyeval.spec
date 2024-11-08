#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lazyeval
Version  : 0.2.2
Release  : 63
URL      : https://cran.r-project.org/src/contrib/lazyeval_0.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lazyeval_0.2.2.tar.gz
Summary  : Lazy (Non-Standard) Evaluation
Group    : Development/Tools
License  : GPL-3.0
Requires: R-lazyeval-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
formulas. Provides a full implementation of LISP style 'quasiquotation',
    making it easier to generate code with other code.

%package lib
Summary: lib components for the R-lazyeval package.
Group: Libraries

%description lib
lib components for the R-lazyeval package.


%prep
%setup -q -c -n lazyeval
cd %{_builddir}/lazyeval

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641045336

%install
export SOURCE_DATE_EPOCH=1641045336
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lazyeval
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lazyeval
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lazyeval
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lazyeval || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lazyeval/DESCRIPTION
/usr/lib64/R/library/lazyeval/INDEX
/usr/lib64/R/library/lazyeval/Meta/Rd.rds
/usr/lib64/R/library/lazyeval/Meta/features.rds
/usr/lib64/R/library/lazyeval/Meta/hsearch.rds
/usr/lib64/R/library/lazyeval/Meta/links.rds
/usr/lib64/R/library/lazyeval/Meta/nsInfo.rds
/usr/lib64/R/library/lazyeval/Meta/package.rds
/usr/lib64/R/library/lazyeval/Meta/vignette.rds
/usr/lib64/R/library/lazyeval/NAMESPACE
/usr/lib64/R/library/lazyeval/NEWS.md
/usr/lib64/R/library/lazyeval/R/lazyeval
/usr/lib64/R/library/lazyeval/R/lazyeval.rdb
/usr/lib64/R/library/lazyeval/R/lazyeval.rdx
/usr/lib64/R/library/lazyeval/doc/index.html
/usr/lib64/R/library/lazyeval/doc/lazyeval-old.R
/usr/lib64/R/library/lazyeval/doc/lazyeval-old.Rmd
/usr/lib64/R/library/lazyeval/doc/lazyeval-old.html
/usr/lib64/R/library/lazyeval/doc/lazyeval.R
/usr/lib64/R/library/lazyeval/doc/lazyeval.Rmd
/usr/lib64/R/library/lazyeval/doc/lazyeval.html
/usr/lib64/R/library/lazyeval/help/AnIndex
/usr/lib64/R/library/lazyeval/help/aliases.rds
/usr/lib64/R/library/lazyeval/help/lazyeval.rdb
/usr/lib64/R/library/lazyeval/help/lazyeval.rdx
/usr/lib64/R/library/lazyeval/help/paths.rds
/usr/lib64/R/library/lazyeval/html/00Index.html
/usr/lib64/R/library/lazyeval/html/R.css
/usr/lib64/R/library/lazyeval/tests/testthat.R
/usr/lib64/R/library/lazyeval/tests/testthat/ast-irregular.txt
/usr/lib64/R/library/lazyeval/tests/testthat/ast-sample.txt
/usr/lib64/R/library/lazyeval/tests/testthat/test-ast.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-call.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-complain.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-dots.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-expr.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-f-capture.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-f-eval.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-f-interp.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-f-list.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-f-unwrap.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-formula.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-function.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-language.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-lazy.R
/usr/lib64/R/library/lazyeval/tests/testthat/test-names.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lazyeval/libs/lazyeval.so
/usr/lib64/R/library/lazyeval/libs/lazyeval.so.avx2
/usr/lib64/R/library/lazyeval/libs/lazyeval.so.avx512
