Name:           gdbm
Url:            http://directory.fsf.org/GNU/gdbm.html
Version:        1.8.3
Release:        0
Summary:        GNU dbm key/data database
License:        GPL-2.0+
Group:          System/Libraries
Source:         ftp://prep.ai.mit.edu/gnu/gdbm/gdbm-%{version}.tar.bz2
Source1001:     gdbm.manifest
Patch0:          gdbm-%{version}.dif
Patch1:         gdbm-protoize_dbm_headers.patch
Patch2:         gdbm-prototype_static_functions.patch
Patch3:         gdbm-fix_testprogs.patch
Patch4:         gdbm-1.8.3-no-build-date.patch
BuildRequires:  libtool

%description
GNU dbm is a library of database functions that use extensible
hashing and work similar to the standard UNIX dbm. These routines are
provided to a programmer needing to create and manipulate a hashed
database.

The basic use of GDBM is to store key/data pairs in a data file. Each
key must be unique and each key is paired with only one data item.

The library provides primitives for storing key/data pairs, searching
and retrieving the data by its key and deleting a key along with its
data. It also supports sequential iteration over all key/data pairs in
a database.

For compatibility with programs using old UNIX dbm functions, the
package also provides traditional dbm and ndbm interfaces.

%package -n libgdbm
Summary:        GNU dbm key/data database
License:        GPL-2.0+
Group:          System/Libraries
# O/P added in 12.2
Obsoletes:      gdbm < %version-%release
Provides:       gdbm = %version-%release

%description -n libgdbm
GNU dbm is a library of database functions that use extensible
hashing and work similar to the standard UNIX dbm. These routines are
provided to a programmer needing to create and manipulate a hashed
database.

The basic use of GDBM is to store key/data pairs in a data file. Each
key must be unique and each key is paired with only one data item.

The library provides primitives for storing key/data pairs, searching
and retrieving the data by its key and deleting a key along with its
data. It also supports sequential iteration over all key/data pairs in
a database.

For compatibility with programs using old UNIX dbm functions, the
package also provides traditional dbm and ndbm interfaces.

%package devel
Summary:        Include Files and Libraries mandatory for Development
License:        GPL-2.0+ ; LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       gdbm = %{version}
Provides:       gdbm:/usr/lib/libgdbm.so

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.


%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4

%build
cp %{S:1001} .
aclocal
%reconfigure --enable-libgdbm-compat --disable-static
make %{?_smp_mflags};

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT
make install-compat INSTALL_ROOT=$RPM_BUILD_ROOT

rm -rf %{buildroot}%{_libdir}/*.la

%remove_docs

%post -n libgdbm -p /sbin/ldconfig

%postun -n libgdbm -p /sbin/ldconfig

%files -n libgdbm
%manifest %{name}.manifest
%doc COPYING
%_libdir/libgdbm.so.3
%_libdir/libgdbm.so.3.0.0
%_libdir/libgdbm_compat.so.3
%_libdir/libgdbm_compat.so.3.0.0

%files devel
%manifest %{name}.manifest
%{_prefix}/include/dbm.h
%{_prefix}/include/gdbm.h
%{_prefix}/include/ndbm.h
%{_prefix}/%{_lib}/libgdbm.so
%{_prefix}/%{_lib}/libgdbm_compat.so
