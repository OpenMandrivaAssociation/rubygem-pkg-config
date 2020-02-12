# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          

%define gem_name pkg-config

Summary:	A pkg-config implementation for Ruby
Name:		rubygem-%{rbname}

Version:	1.4.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://github.com/rcairo/pkg-config
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:  pkgconfig(ruby)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  ruby
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

%gem_install -n %{SOURCE0}

%build
#nothing

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir}

cp -a .%{gem_dir}/* \
    %{buildroot}/%{gem_dir}/

%files
%dir %{gem_dir}/gems/%{gem_name}-%{version}/lib
%{gem_dir}/gems/%{gem_name}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{gem_name}-%{version}/lib/pkg-config
%{gem_dir}/gems/%{gem_name}-%{version}/lib/pkg-config/*.rb
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%{gem_dir}/gems/%{gem_name}-%{version}/test/*
%{gem_dir}/cache/*
%exclude	%{gem_dir}/gems/%{gem_name}-%{version}/Rakefile
%exclude	%{gem_dir}/gems/%{gem_name}-%{version}/setup.rb

%doc	%{gem_dir}/gems/%{gem_name}-%{version}/[A-Z]*

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}


