Summary:	System logs monitor and security violations detection tool
Summary(pl.UTF-8):	Monitor logów oraz narzędzie wykrywające naruszenia bezpieczeństwa
Name:		logsentry
Version:	1.1.1
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	http://www.psionic.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	e97c2f096e219e20310c1b80e9e1bc29
Source1:	%{name}.cron
Patch0:		%{name}-pld.patch
URL:		http://www.psionic.com/products/
Requires:	/bin/mail
Requires:	crondaemon
Requires:	fileutils
Requires:	net-tools
Requires:	sh-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/logsentry

%description
LogSentry is part of the Abacus Project suite of tools. The Abacus
Project is an initiative to release low-maintenance, generic, and
reliable host based intrusion detection software to the Internet
community.

%description -l pl.UTF-8
LogSentry jest częścią zestawu narzędzi Projektu Abacus. Projekt
Abacus ma na celu stworzenie ogólnego, pewnego i wymagającego
niewielkiej obsługi oprogramowania do wykrywania prób skanowania
portów dla internetowej społeczności.

%prep
%setup  -q -n logcheck-%{version}
%patch -P0 -p0

%build
%{__cc} %{rpmcflags} -Wall -o src/logtail src/logtail.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},/etc/cron.d}

install systems/linux/logcheck.{hacking,ignore,violations{,.ignore}} $RPM_BUILD_ROOT%{_sysconfdir}
install systems/linux/logcheck.sh $RPM_BUILD_ROOT%{_sbindir}
install src/logtail $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS INSTALL README* systems/linux/README.linux.IMPORTANT
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) /etc/cron.d/*
