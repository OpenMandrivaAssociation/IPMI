%define	name	IPMI
%define	version	1.0 
%define	release	%mkrel 12

Summary:	A simple initscript to load IPMI drivers
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ipmi
License:	GPL
Group:		System/Kernel and hardware 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post,preun):	rpm-helper, openipmi-lanserv
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


%changelog
* Fri Apr 15 2011 Antoine Ginies <aginies@mandriva.com> 1.0-12mdv2011.0
+ Revision: 653142
- bump the release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-11mdv2010.1
+ Revision: 521841
- rebuilt for 2010.1

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-10mdv2010.0
+ Revision: 423657
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0-9mdv2009.0
+ Revision: 221634
- rebuild
- fix no-buildroot-tag

* Tue Feb 05 2008 Erwan Velu <erwan@mandriva.org> 1.0-8mdv2008.1
+ Revision: 162680
- Fixing typo
- Fixing requires

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0-7mdv2008.1
+ Revision: 150292
- rebuild
- fix prereq on rpm-helper
- kill re-definition of %%buildroot on Pixel's request

* Wed May 02 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-6mdv2008.0
+ Revision: 20291
- support pinit; rebuild for new era
- Import IPMI



* Mon Mar 20 2006 Erwan Velu <erwan@seanodes.com> 1.0-5mdk
- mkrel
- rebuild

* Tue Aug 24 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0-4mdk
- fix typo in init script
- cosmetics

* Wed Aug 18 2004 Erwan Velu <erwan@mandrakesoft.com> 1.0-3mdk
- Supporting 2.4 kernels
- Supporting v32 & V30 under 2.6 kernels

* Fri Aug 13 2004 Erwan Velu <erwan@mandrakesoft.com> 1.0-2mdk
- Fixing description

* Wed Aug 11 2004 Erwan Velu <erwan@mandrakesoft.com> 1.0-1mdk
- Initial relase
