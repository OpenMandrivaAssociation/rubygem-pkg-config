# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	pkg-config

Summary:	A pkg-config implementation for Ruby
Name:		rubygem-%{rbname}

Version:	1.1.4
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://github.com/rcairo/pkg-config
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
pkg-config can be used in your extconf.rb to properly detect need libraries
for compiling Ruby native extensions

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
#%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/pkg-config
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/pkg-config/*.rb
#%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
#%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}

%changelog

