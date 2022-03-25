Summary:	Command line util which allows to draw images on terminals
Name:		ueberzug
Version:	18.1.9
Release:	4
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://github.com/seebye/ueberzug/archive/%{version}/%{name}-%{version}.tar.gz 
# Source0-md5:	9d6ee6e2ef75c68e318bdb224be71af1
URL:		https://github.com/seebye/ueberzug
Patch0:		single_process_terminals.patch
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.720
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Überzug is a command line util which allows to draw images on
terminals by using child windows.

%prep
%setup -q
%patch0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/ueberzug
%attr(755,root,root) %{py3_sitedir}/Xshm.cpython-3*.so
%dir %{py3_sitedir}/ueberzug
%{py3_sitedir}/ueberzug/*.py
%{py3_sitedir}/ueberzug/__pycache__
%{py3_sitedir}/ueberzug-%{version}-py*.egg-info
%{py3_sitedir}/ueberzug/lib
