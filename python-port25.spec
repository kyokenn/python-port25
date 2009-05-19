%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
# Done to avoid duplication of information
%{!?app_name: %define app_name %(%{__python} setup.py --name)}
%{!?app_version: %define app_version %(%{__python} setup.py --version)}
%{!?app_summary: %define app_summary %(%{__python} setup.py --description)}
%{!?app_description: %define app_description %(%{__python} setup.py --long-description)}
%{!?app_license: %define app_license %(%{__python} setup.py --license)}
%{!?app_url: %define app_url %(%{__python} setup.py --url)}

Name:           %{app_name}
Version:        %{app_version}
Release:        1%{?dist}
Summary:        %{app_summary}

Group:          Development/Libraries
License:        %{app_license}
URL:            %{app_url}
Source0:	http://python-port25.googlecode.com/files/python-port25-0.0.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       python >= 2.3 PowerMTA


%description
%{app_description}


%prep
%setup -q -n python-port25-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc INSTALL LICENSE AUTHORS COPYING examples/
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
