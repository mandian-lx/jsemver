%{?_javapackages_macros:%_javapackages_macros}

Name:           jsemver
Version:        0.9.0
Release:        4%{?dist}
Summary:        A Java implementation of the Semantic Versioning Specification

License:        MIT
URL:            https://github.com/zafarkhaja/jsemver
Source0:        https://github.com/zafarkhaja/jsemver/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin >= 3.2
BuildRequires:  maven-javadoc-plugin >= 2.10.1
BuildRequires:  junit >= 4.12

%description
JSemVer (formerly Java SemVer) is a Java implementation of
version 2.0.0 of the Semantic Versioning Specification

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q
find -name \*.jar -delete
find -name \*.class -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}
%doc CHANGELOG.md
%doc README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May  5 2015 Neal Gompa <ngompa13{%}gmail{*}com> - 0.9.0-1
- Update to upstream version 0.9.0

* Wed Apr  8 2015 Neal Gompa <ngompa13{%}gmail{*}com> - 0.8.0-1
- Added extra prep step to delete *.class/*.jar files
- Added statement to own maven pom dir
- Removed duplicate doc files from -javadoc
- Removed license file going into doc
- Removed unnecessary epoch
- Initial Packaging
