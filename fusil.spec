%define name 	fusil
%define version 1.3.2
%define release %mkrel 2

Summary: 	Framework for fuzzing
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Development/Other
URL: 		http://fusil.hachoir.org/trac
Source0: 	http://pypi.python.org/packages/source/f/%{name}/%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: 	noarch
BuildRequires: 	python-devel
Requires: 	python python-ptrace

%description
Fusil the fuzzer is a Python library used to write fuzzing programs.
It helps to start process with a prepared environment (limit memory,
environment variables, redirect stdout, etc.), start network client
or server, and create mangled files. Fusil has many probes to detect
program crash: watch process exit code, watch process stdout and
syslog for text patterns (eg. "segmentation fault"), watch session
duration, watch cpu usage (process and system load), etc.

%prep
%setup -q


%build
python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=%{buildroot}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL README README.windows.txt TODO
%{_bindir}/%{name}-*
%py_puresitedir/%{name}
%py_puresitedir/*.egg-info



%changelog
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 1.3.2-2mdv2011.0
+ Revision: 590157
- rebuild for python 2.7

* Thu Feb 04 2010 Michael Scherer <misc@mandriva.org> 1.3.2-1mdv2010.1
+ Revision: 500615
- update to new version 1.3.2

* Tue Nov 10 2009 Michael Scherer <misc@mandriva.org> 1.3.1-1mdv2010.1
+ Revision: 463857
- update to new version 1.3.1

* Wed Sep 23 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3-1mdv2010.0
+ Revision: 448007
- update to new version 1.3

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-2mdv2010.0
+ Revision: 437609
- rebuild

* Tue Feb 17 2009 Jérôme Soyer <saispo@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 341620
- New upstream release

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.1-2mdv2009.1
+ Revision: 325569
- rebuild

* Wed Nov 19 2008 trem <trem@mandriva.org> 1.1-1mdv2009.1
+ Revision: 304779
- new release 1.1

* Sat Sep 13 2008 Michael Scherer <misc@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 284413
- new version 1.0

* Mon Jul 28 2008 Michael Scherer <misc@mandriva.org> 0.9.1-1mdv2009.0
+ Revision: 251264
- update to new version 0.9.1
- use the correct source url for mdvsys update

* Wed Jul 16 2008 Michael Scherer <misc@mandriva.org> 0.9-2mdv2009.0
+ Revision: 236563
- add requires on python-ptrace, as reported by Victor Stinner

* Thu Jul 10 2008 trem <trem@mandriva.org> 0.9-1mdv2009.0
+ Revision: 233522
- update to 0.9
- import fusil

  + Michael Scherer <misc@mandriva.org>
    - add projects directory to have useful examples


* Sun Mar 16 2008 trem <trem@mandriva.org> 0.7-1mdv2008.1
- Initial build.
