# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	pkg-config

Summary:	A pkg-config implementation for Ruby
Name:		rubygem-%{rbname}

Version:	1.3.8
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://github.com/rcairo/pkg-config
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems-devel
BuildRequires:	ruby-psych
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
%setup -q -c -T

%build
#nothing

%install
%gem_install -n %{SOURCE0}

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/pkg-config
%{gem_dir}/gems/%{rbname}-%{version}/lib/pkg-config/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}


