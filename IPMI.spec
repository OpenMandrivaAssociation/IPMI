Summary:	A simple initscript to load IPMI drivers
Name:		IPMI
Version:	1.0
Release:	21
License:	GPLv2
Group:		System/Kernel and hardware 
Source0:	ipmi
BuildArch:	noarch
Requires(post,preun):	openipmi-lanserv
Requires(post,preun):	rpm-helper

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
install -m744 %{SOURCE0} -D %{buildroot}%{_initrddir}/ipmi

%post
%_post_service ipmi

%preun
%_preun_service ipmi

%files
%config(noreplace) %{_initrddir}/ipmi

