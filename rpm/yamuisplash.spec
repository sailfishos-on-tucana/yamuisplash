Name:		yamuisplash
Summary:	Simple splash screen for SailfishOS
Version:	1.0.0
Release:	1
Url:		https://github.com/sailfishos/yamuisplash
License:	ASL 2.0
Source0:	%{name}-%{version}.tar.gz

Conflicts:	qmlsplash
Requires:	yamui
BuildRequires:	systemd

%description
Yamuisplash is a simple splash screen for SailfishOS.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to do here

%install
install -D -m 744 yamuisplash $RPM_BUILD_ROOT%{_bindir}/yamuisplash
install -D -m 644 logo/sailfish_logo_rgb.png $RPM_BUILD_ROOT%{_datarootdir}/%{name}/sailfish_logo_rgb.png
install -D -m 644 systemd/yamuisplash.service $RPM_BUILD_ROOT%{_unitdir}/yamuisplash.service

install -d $RPM_BUILD_ROOT/%{_unitdir}/graphical.target.wants
ln -s ../yamuisplash.service $RPM_BUILD_ROOT%{_unitdir}/graphical.target.wants/yamuisplash.service

install -d $RPM_BUILD_ROOT/%{_unitdir}/system-update-pre.target.wants
ln -s ../yamuisplash.service $RPM_BUILD_ROOT%{_unitdir}/system-update-pre.target.wants/yamuisplash.service

install -d $RPM_BUILD_ROOT/%{_unitdir}/sailfish-unlock-agent.service.d
cp systemd/01-yamuisplash.conf $RPM_BUILD_ROOT%{_unitdir}/sailfish-unlock-agent.service.d/

install -d $RPM_BUILD_ROOT/%{_unitdir}/systemd-user-sessions.service.d
cp systemd/01-yamuisplash.conf $RPM_BUILD_ROOT%{_unitdir}/systemd-user-sessions.service.d/

%files
%defattr(-,root,root,-)
%license LICENSE-2.0.txt
%{_unitdir}/%{name}.service
%{_unitdir}/graphical.target.wants/%{name}.service
%{_unitdir}/system-update-pre.target.wants/%{name}.service
%{_datarootdir}/%{name}/sailfish_logo_rgb.png
%{_unitdir}/sailfish-unlock-agent.service.d/01-yamuisplash.conf
%{_unitdir}/systemd-user-sessions.service.d/01-yamuisplash.conf
%{_bindir}/yamuisplash
