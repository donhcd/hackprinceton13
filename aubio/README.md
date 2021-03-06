aubio library
=============

aubio is a library to label music and sounds. It listens to audio signals and
attempts to detect events. For instance, when a drum is hit, at which frequency
is a note, or at what tempo is a rhythmic melody.

Its features include segmenting a sound file before each of its attacks,
performing pitch detection, tapping the beat and producing midi streams from
live audio.

aubio provide several algorithms and routines, including:

  - several onset detection methods
  - different pitch detection methods
  - tempo tracking and beat detection
  - MFCC (mel-frequency cepstrum coefficients)
  - FFT and phase vocoder
  - up/down-sampling
  - digital filters (low pass, high pass, and more)
  - spectral filtering
  - transient/steady-state separation
  - sound file and audio devices read and write access
  - various mathematics utilities for music applications

The name aubio comes from _audio_ with a typo: some errors are likely to be
found in the results.


Implementation and Design Basics
--------------------------------

The library is written in C and is optimised for speed and portability. A
python module to access the library functions is also provided. A few simple
applications are included along with the library:

 - `aubioonset` outputs the time stamp of detected note onsets
 - `aubiotempo` does the same for the tempo
 - `aubionotes` emits midi-like notes, with an onset, a pitch, and a duration
 - `aubiocut` slices an input sound and cuts it in several smaller files, sliced
   at each detected onset or beat
 - `aubiopitch` attempts to identify a fundamental frequency, or pitch, for each
   frame of the input sound

The C API is designed in the following way:

    aubio_something_t * new_aubio_something (void * args);
    audio_something_do (aubio_something_t * t, void * args);
    smpl_t aubio_something_get_a_parameter (aubio_something_t *t);
    uint_t aubio_something_set_a_parameter (aubio_something_t *t, smpl_t a_parameter);
    void del_aubio_something (aubio_something_t * t);

For performance and real-time operation, no memory allocation or freeing take
place in the `_do` methods. Instead, memory allocation should always take place
in the `new_` methods, whereas free operations are done in the `del_` methods.


Installation and Build Instructions
-----------------------------------

A number of distributions already include aubio. Check your favorite package
management system, or have a look at the [download
page](http://aubio.org/download).

aubio uses [waf](https://code.google.com/p/waf/) to configure, compile, and
test the source:

    ./waf configure
    ./waf build
    sudo ./waf install

aubio compiles on Linux, Mac OS X, Cygwin, and iPhone.


Credits and Publications
------------------------

This library gathers music signal processing algorithms designed at the Centre
for Digital Music and elsewhere. This software project was developed along the
research I did at the Centre for Digital Music, Queen Mary, University of
London. Most of this C code was written by myself, starting from published
papers and existing code. The header files of each algorithm contains brief
descriptions and references to the corresponding papers.

Special thanks go Juan Pablo Bello, Chris Duxbury, Samer Abdallah, Alain de
Cheveigne for their help and publications. Also many thanks to Miguel Ramirez
and Nicolas Wack for their bug fixing.

Substantial informations about the algorithms and their evaluation are gathered
in:

  - Paul Brossier, _[Automatic annotation of musical audio for interactive
    systems](http://aubio.org/phd)_, PhD thesis, Centre for Digital music,
Queen Mary University of London, London, UK, 2006.

Additional results obtained with this software were discussed in the following
papers:

  - P. M. Brossier and J. P. Bello and M. D. Plumbley, [Real-time temporal
    segmentation of note objects in music signals](http://aubio.org/articles/brossier04fastnotes.pdf),
in _Proceedings of the International Computer Music Conference_, 2004, Miami,
Florida, ICMA

  -  P. M. Brossier and J. P. Bello and M. D. Plumbley, [Fast labelling of note
     objects in music signals] (http://aubio.org/articles/brossier04fastnotes.pdf),
in _Proceedings of the International Symposium on Music Information Retrieval_,
2004, Barcelona, Spain


Contact Info and Mailing List
-----------------------------

The home page of this project can be found at: http://aubio.org/

Questions, comments, suggestions, and contributions are welcome. Use the
mailing list: <aubio-user@aubio.org>.

To subscribe to the list, use the mailman form:
http://lists.aubio.org/listinfo/aubio-user/

Alternatively, feel free to contact directly the author.


Copyright and License Information
---------------------------------

Copyright (C) 2003-2013 Paul Brossier <piem@aubio.org>

aubio is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
