%define name 	fusil
%define version 1.2.1
%define release %mkrel 1

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

