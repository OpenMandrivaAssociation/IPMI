%define	name	IPMI
%define	version	1.0 
%define	release	%mkrel 6

Summary:	A simple initscript to load IPMI drivers
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ipmi
License:	GPL
Group:		System/Kernel and hardware 
Requires(post,preun):	rpm-helper
buildarch:	noarch

%description
A simple initscript to load IPMI drivers
IPMI stands for Intelligent Platform Management Interface
and is an open standard for machine health, and control
(including remote control), and is implemented by many
hardware vendors - Intel is one of the originators
and early adopters of the standard.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -m744 %{SOURCE0} -D $RPM_BUILD_ROOT%{_initrddir}/ipmi

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_post_service ipmi

%preun
%_preun_service ipmi

%files
%defattr(-,root,root)
%config(noreplace) %{_initrddir}/ipmi
