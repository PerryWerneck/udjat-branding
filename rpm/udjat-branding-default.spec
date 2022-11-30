#
# spec file for package libudjat
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (C) <2008> <Banco do Brasil S.A.>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define product_name %(pkg-config --variable=product_name libudjat)
%define httproot /srv/www/htdocs/%{product_name}

Summary:		Branding for libudjat applications 
Name:			udjat-branding-default
Version:		1.0
Release:		0
License:		LGPL-3.0
Source:			%{name}-%{version}.tar.xz

URL:			https://github.com/PerryWerneck/udjat-module-network

Group:			Development/Libraries/C and C++
BuildRoot:		/var/tmp/%{name}-%{version}
BuildArch:		noarch

Requires:		libudjat1_0

Provides:		udjat-branding = %{version}
Conflicts:		otherproviders(udjat-branding)

Supplements:	packageand(udjat:branding-default)

BuildRequires:  pkgconfig(libudjat)
BuildRequires:	fdupes

# Python scour & pre-reqs
BuildRequires:	python-setuptools
BuildRequires:	python-xml
BuildRequires:	python-scour
#BuildRequires:	python3-css-html-js-minify

%description
Branding default for libudjat applications.

#---[ Build & Install ]-----------------------------------------------------------------------------------------------

%prep
%setup

%build

%install

mkdir -p %{buildroot}%{httproot}/icons
for SVG in icons/*.svg
do
	scour -i "${SVG}" -o "%{buildroot}%{httproot}/icons/$(basename ${SVG})"
	chmod 644 "%{buildroot}%{httproot}/icons/$(basename ${SVG})"
done


%fdupes %{buildroot}/%{httproot}

%files
%defattr(-,root,root)
%dir %{httproot}
%dir %{httproot}/icons

%{httproot}/icons/*.svg

%changelog
