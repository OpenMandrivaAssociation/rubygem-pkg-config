# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
Summary:	A pkg-config implementation for Ruby
Name:		rubygem-pkg-config
Version:	1.4.6
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://github.com/rcairo/pkg-config
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:  pkgconfig(ruby)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  ruby
BuildArch:	noarch

%description
pkg-config can be used in your extconf.rb to properly detect need libraries
for compiling Ruby native extensions

%prep
%autosetup -p1 -n %{gem_name}-%{version}

%build
%gem_build

%install
%gem_install

%files
%{gem_files}
