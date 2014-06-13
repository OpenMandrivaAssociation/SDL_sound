%define major 1
%define apiver 1.0
%define libname %mklibname %{name} %{apiver} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -d -s
%define oldlibname %mklibname %{name} 1.0

Summary:	An abstract SDL soundfile decoder
Name:		SDL_sound
Version:	1.0.3
Release:	16
Group:		Sound
License:	LGPLv2+
URL:		http://www.icculus.org/SDL_sound
Source:		http://www.icculus.org/SDL_sound/downloads/%{name}-%{version}.tar.gz
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
%setup -q
%patch0 -p1

%build
export CPPFLAGS="-I%{_includedir}/libmodplug"
%configure2_5x
%make
doxygen

%install
%__rm -rf %{buildroot}
%makeinstall_std

%if "%{_lib}" == "lib64"
perl -pi -e "s|-L/usr/lib\b|-L%{_libdir}|g" %{buildroot}%{_libdir}/*.la
%endif

%clean
%__rm -rf %{buildroot}

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
%{_includedir}/SDL/*

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/lib*.a


%changelog
* Sat Mar 31 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.0.3-10
+ Revision: 788446
- Get rid of harmful .la files
- Clean up spec file

* Thu Jan 19 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.3-9
+ Revision: 762342
- Rebuild for .la files issue, spec cleanup

* Mon Jun 20 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-8
+ Revision: 686305
- avoid pulling 32 bit libraries on 64 bit arch

* Sun Jul 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.3-7mdv2011.0
+ Revision: 550632
- rebuild for new libmodplug

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 1.0.3-6mdv2010.1
+ Revision: 500133
- rebuild

* Fri Oct 02 2009 Funda Wang <fwang@mandriva.org> 1.0.3-5mdv2010.0
+ Revision: 452455
- fix build

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - rebuild for latest libphysfs

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Aug 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.3-3mdv2009.0
+ Revision: 271798
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-2mdv2009.0
+ Revision: 266092
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 29 2008 Funda Wang <fwang@mandriva.org> 1.0.3-1mdv2009.0
+ Revision: 213007
- New version 1.0.3
-drop old patches

* Fri Jan 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.1-18mdv2008.1
+ Revision: 154553
- fix obsoletes again

* Thu Jan 17 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.1-17mdv2008.1
+ Revision: 154000
- fix deps of the static devel package

  + Anssi Hannula <anssi@mandriva.org>
    - obsolete old library name

* Tue Jan 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-15mdv2008.1
+ Revision: 152282
- new license policy
- new devel library policy
- do not package COPYING file
- drop br on automake-1.7
- obsolete old library name

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 31 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.0.1-13mdv2008.0
+ Revision: 33476
- Rebuild with libslang2.


* Thu Feb 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.1-12mdv2007.0
+ Revision: 124392
- fix build with libmodplug

* Mon Dec 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.1-11mdv2007.1
+ Revision: 94966
- Import SDL_sound

* Mon Dec 11 2006 Götz Waschk <waschk@mandriva.org> 1.0.1-11mdv2007.1
- patch for new flac

* Sat Sep 09 2006 Götz Waschk <waschk@mandriva.org> 1.0.1-10mdv2007.0
- rebuild for new libphysfs

* Tue Aug 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.1-1mdv2007.0
- rebuild for new libphysfs

* Wed Jun 07 2006 Götz Waschk <waschk@mandriva.org> 1.0.1-8mdv2007.0
- Rebuild
- use mkrel

* Sat Jun 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.1-7mdk
- Rebuild

* Tue Apr 19 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.0.1-6mdk
- rebuild with new libflac

* Sat Nov 13 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-5mdk
- rebuild

* Fri Nov 12 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-4mdk
- rebuild

* Tue Aug 03 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-3mdk
- rebuild for new flac

* Sat Jun 26 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-2mdk
- rebuild for new physfs

