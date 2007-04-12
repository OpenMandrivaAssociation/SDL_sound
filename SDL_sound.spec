%define name SDL_sound
%define version 1.0.1
%define release %mkrel 12
%define libname %mklibname %name 1.0

Summary: SDL_sound. An abstract soundfile decoder
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://www.icculus.org/SDL_sound/downloads/%{name}-%{version}.tar.bz2
Patch: SDL_sound-1.0.1-smpeg.m4.patch
Patch1: SDL_sound-1.0.1+flac-1.1.3.patch
URL: http://www.icculus.org/SDL_sound
License: LGPL
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: SDL-devel
BuildRequires: libflac-devel
BuildRequires: smpeg-devel >= 0.4.4-23mdk
BuildRequires: libmikmod-devel
BuildRequires: libmodplug-devel
BuildRequires: libvorbis-devel
BuildRequires: libspeex-devel
BuildRequires: physfs-devel
BuildRequires: doxygen
BuildRequires: automake1.7

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


%package -n %libname
Summary:	SDL graphics drawing primitives and other support functions
Group:		System/Libraries

%description -n %libname
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

%package -n %libname-devel
Summary:	Header files and more to develop SDL_sound applications
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %version-%release
Provides:	%name-devel = %version-%release

%description -n %libname-devel
Header files and more to develop SDL_sound applications.

%package -n %libname-static-devel
Summary:	Static SDL_sound libraries
Group:		Development/C
Requires:	%{libname}-devel = %{version}

%description -n %libname-static-devel
Static SDL_sound libraries.

%prep
%setup -q
%patch -p1 -b .smpeg
%patch1 -p1 -b .flac
aclocal-1.7
automake-1.7 --foreign
autoconf

%build
export CPPFLAGS="-I%_includedir/libmodplug"
%configure2_5x
%make
doxygen

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README
%_bindir/playsound

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%doc CHANGELOG COPYING TODO CREDITS docs/html
%{_libdir}/lib*.so
%attr(644,root,root) %{_libdir}/lib*.la
%{_includedir}/SDL/*

%files -n %libname-static-devel
%defattr(-,root,root)
%{_libdir}/lib*.a


