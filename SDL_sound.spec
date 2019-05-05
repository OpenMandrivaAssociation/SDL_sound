%define major 1
%define apiver 1.0
%define libname %mklibname %{name} %{apiver} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -d -s
%define oldlibname %mklibname %{name} 1.0
%define _disable_lto 1

Summary:	An abstract SDL soundfile decoder
Name:		SDL_sound
Version:	1.0.3
Release:	24
Group:		Sound
License:	LGPLv2+
URL:		http://www.icculus.org/SDL_sound
Source0:	http://www.icculus.org/SDL_sound/downloads/%{name}-%{version}.tar.gz
Patch0:		SDL_sound-1.0.3-linkage.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(flac)
BuildRequires:	libmikmod-devel
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(speex)
BuildRequires:	physfs-devel
BuildRequires:	doxygen

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
Obsoletes:	%{oldlibname} < 1.0.1-15

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
Obsoletes:	%{oldlibname}-devel < 1.0.1-15

%description -n %{develname}
Header files and more to develop SDL_sound applications.

%package -n %{staticname}
Summary:	Static SDL_sound libraries
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Obsoletes:	%{oldlibname}-static-devel < 1.0.1-15

%description -n %{staticname}
Static SDL_sound libraries.

%prep
%autosetup -p1

%build
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
touch NEWS AUTHORS ChangeLog
autoreconf -fi
export CPPFLAGS="-I%{_includedir}/libmodplug -D__EXPORT__="
%global ldflags %{ldflags} -lm

%configure --enable-static
%make_build
doxygen

%install
%make_install

%if "%{_lib}" == "lib64"
sed -i -e "s|-L/usr/lib\b|-L%{_libdir}|g" %{buildroot}%{_libdir}/*.la
%endif

%files
%doc README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/lib*%{apiver}.so.%{major}*

%files -n %{develname}
%doc CHANGELOG TODO CREDITS docs/html
%{_libdir}/lib*.so
%{_includedir}/SDL/*

%files -n %{staticname}
%{_libdir}/lib*.a
