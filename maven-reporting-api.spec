Name:		maven-reporting-api
Version:	4.1.0
Release:	1
Epoch:		1
Summary:	Maven reporting API
Group:		Development/Java
License:	Apache-2.0
URL:		https://maven.apache.org/shared/maven-reporting-api/
Source0:	https://github.com/apache/maven-reporting-api/archive/refs/tags/maven-reporting-api-%{version}.tar.gz
BuildArch:	noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	maven-shared
BuildRequires:	doxia-sink-api >= 2.2.0
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

# The previous package was 1:3.0. Epoch stays 1 so this stays ahead of it.
Obsoletes:	maven-shared-reporting-api < %{EVRD}
Provides:	maven-shared-reporting-api = %{EVRD}

%description
API for Maven report generation. The only compile dependency is the
Doxia sink API. 4.1.0 adds MavenReport.generate(Sink, SinkFactory, Locale)
as a default method, deprecates MavenMultiPageReport, and builds
against Doxia sink API 2.2.0.

%prep
%autosetup -n maven-reporting-api-maven-reporting-api-%{version}

%files -f .mfiles
%doc LICENSE README.md
