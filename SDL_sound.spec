%define major 1
%define apiver 1.0
%define libname %mklibname %name %{apiver} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -d -s
%define oldlibname %mklibname %name 1.0

Summary:	An abstract SDL soundfile decoder
Name:		SDL_sound
Version:	1.0.3
Release:	%mkrel 1
Group:		Sound
License:	LGPLv2+
URL:		http://www.icculus.org/SDL_sound
Source:		http://www.icculus.org/SDL_sound/downloads/%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel
BuildRequires:	libflac-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libspeex-devel
BuildRequires:	physfs-devel
BuildRequires:	doxygen
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as .WAV and .MP3. It is meant to make the
programmer's sound playback tasks simpler. The programmer gives
SDL_sound a filename, or feeds it data directly from one of many
sources, and then reads the decoded waveform data back at her
leisure. If resource constraints are a concern, SDL_sound can process
sound data in programmer-specified blocks. Alternately, SDL_sound can
decode a whole sound file and hand back a single pointer to the whole
waveform. SDL_sound can also handle sample rate, audio format, and
channel conversion on-the-fly and behind-the-scenes, if the programmer
desires.


%package -n %{libname}
Summary:	SDL graphics drawing primitives and other support functions
Group:		System/Libraries
Obsoletes:	%oldlibname < 1.0.1-15

%description -n %{libname}
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as .WAV and .MP3. It is meant to make the
programmer's sound playback tasks simpler. The programmer gives
SDL_sound a filename, or feeds it data directly from one of many
sources, and then reads the decoded waveform data back at her
leisure. If resource constraints are a concern, SDL_sound can process
sound data in programmer-specified blocks. Alternately, SDL_sound can
decode a whole sound file and hand back a single pointer to the whole
waveform. SDL_sound can also handle sample rate, audio format, and
channel conversion on-the-fly and behind-the-scenes, if the programmer
desires.

%package -n %{develname}
Summary:	Header files and more to develop SDL_sound applications
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%oldlibname-devel < 1.0.1-15

%description -n %{develname}
Header files and more to develop SDL_sound applications.

%package -n %{staticname}
Summary:	Static SDL_sound libraries
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Obsoletes:	%oldlibname-static-devel < 1.0.1-15

%description -n %{staticname}
Static SDL_sound libraries.

%prep
%setup -q
aclocal
automake --foreign
autoconf

%build
export CPPFLAGS="-I%{_includedir}/libmodplug"
%configure2_5x
%make
doxygen

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*%{apiver}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc CHANGELOG TODO CREDITS docs/html
%{_libdir}/lib*.so
%attr(644,root,root) %{_libdir}/lib*.la
%{_includedir}/SDL/*

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/lib*.a
