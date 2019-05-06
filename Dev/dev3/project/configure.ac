#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([lame_project], [1.0])
AM_INIT_AUTOMAKE([1.9 foreign])
AC_CONFIG_SRCDIR([src/lib_foo/foo.c])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_CC

# Checks for libraries.
AC_PROG_RANLIB
AC_SEARCH_LIBS([mistery_value],[magic voodoo mistery],[],[AC_MSG_ERROR([Unable to find correct libraries])])

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions, and use easter eggm
AC_COMPILE_IFELSE( [AC_LANG_PROGRAM( [[#include <mistery.h>]], [[mistery_value(5941)]] )], [AC_DEFINE( [MISTERY_VALUE_ONEPARAM],[],[Only one arg for mistery_function] )], [] )


AC_CONFIG_FILES([Makefile src/Makefile src/lib_foo/Makefile src/main/Makefile])

AC_OUTPUT
