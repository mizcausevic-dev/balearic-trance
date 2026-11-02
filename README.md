# Balearic Trance

Original note-only MIDI construction kits. Four kits, six core parts, two variations of each part. The parts are drums, bass, harmonic keys, motif, sequence, and pad. Bass, motif, and sequence are monophonic. Each 32-bar arrangement states a theme, develops a sequence, opens to a sparse section, and returns the motif.

This repository is the pack. The GitHub repository is https://github.com/mizcausevic-dev/balearic-trance and it is public. The catalog address is https://mizcausevic-dev.github.io/balearic-trance/ . Treat that host as live only after it responds.

## What you can open

- `index.html` is the file catalog. Pick a kit, then variation A or B. The lanes are drawn from the fetched MIDI.
- `media.html` is the stills page. The film sits under the pictures.
- Each kit has a 32-bar Format 1 arrangement under `midi/`. Kit 01 is `midi/k01-salt-terrace/arrangement.mid`.
- Individual Format 0 parts live beside that arrangement.
- `midi/validation-Cursor.json` is the report from reopening those exact bytes.
- `preview/preview.mp3` is the primary music preview. It is 30.000 seconds in the encoded file. preview, not a master.
- `film/preview.mp4` and `film/preview.vtt` are the film. On-picture and caption text is `preview, not master`.
- `art/hero.jpg` is a 1280x720 illustration. `art/square.jpg` is 1080x1080. Neither is a photograph.

Use either the combined arrangement or the separate parts. Do not stack the part files on top of the combined file.

## Kits

- k01 Salt Terrace: 128 BPM, 8 bar parts, 32 bar arrangement, D Mixolydian, tonic D.
- k02 White Cove: 126 BPM, 8 bar parts, 32 bar arrangement, A major, tonic A.
- k03 Glass Room: 132 BPM, 8 bar parts, 32 bar arrangement, G Lydian, tonic G.
- k04 Ferry Light: 136 BPM, 8 bar parts, 32 bar arrangement, F major, tonic F.

Core files: 48. Reference files: 0.

Drums use MIDI channel index 9, the GM channel 10, and only the mapped pitches 36 kick, 37 side stick, 38 acoustic snare, 39 clap, 40 electric snare, 42 closed hat, 46 open hat, and 49 crash. Bass is monophonic, MIDI 41 to 62, channel 1, and it avoids the drum pitches. Harmonic keys allow four notes, MIDI 48 to 76, channel 2. Motif is monophonic, MIDI 60 to 86, channel 3. Sequence is monophonic, MIDI 52 to 81, channel 4. Pad allows four notes, MIDI 48 to 81, channel 5. C4 is 60. PPQ is 960. Meter is 4/4. A bar is 3840 ticks. Offsets are 0. Seeds identify kits and are not random draws. Generator 1.0.0.

Every arrangement is theme, sequence, open, return. The open section is thinner and has no drums, bass, or motif. The return restates motif A. Motif and sequence do not share a section. A bar stays 3840 ticks.

- k01: Keys A changes chord every two bars: D dominant seventh, C major seventh, G major seventh, A minor seventh.
- k02: Keys A is A major seventh, D major, E major, then F# minor, two bars each.
- k03: Keys A bars 1-4 are G major seventh. Bars 5-8 are D major seventh.
- k04: Keys A is Bb major seventh, F major, D minor seventh, then C major.

## Preview path

The preview renders bars 17-32 of the kit 01 arrangement with `simple-synth-1.0.0`. That is an excerpt. Those bars are the open section and the return. The return restates the motif. The arrangement is 32 bars, score length 60.000 seconds, which is past the 40 second preview limit. The excerpt score length is 30.000 seconds. Tempo authority is the encoded microsecond value in the MIDI, 468750 us per quarter note. Excerpt tick 0 is arrangement tick 61440. Sample positions use `floor(seconds * 44100 + 0.5)` from that excerpt tick. Intervals are not summed. Sample-exact repeating loops at an arbitrary BPM are not promised.

The synth mapping is a simple-synth: kick and noise drums, a dull saw bass, a soft tone for harmonic keys, a triangle for the sequence, a sine for the motif, and a slow tone for the pad. Filter motion and chorus width are not in the MIDI. No program changes are encoded. A conventional GM player will normally use its default piano program for pitched channels unless configured otherwise; compatible GM channel 10 percussion is treated separately. Player behavior may vary. The mapping is not encoded in the MIDI.

Encoded MP3 settings: libmp3lame, 192 kbps. Film audio is AAC at 160 kbps re-encoded from that MP3, so the decoded film audio is not byte-identical to the MP3. Film duration probe: 30.000 seconds. MP3 container probe 30.000 seconds. MP4 probe 30.000 seconds. The film ends on a video frame, so it is slightly shorter than the MP3 container. The music is the same preview, not a different excerpt. The picture is a still illustration with rasterized disclosure text. DejaVu Sans Bold from the build machine supplies the glyphs. The font file is not in this pack.

No human listening audition was performed for this build. A sample peak is recorded in the preview manifest. It is not a loudness measurement and it is not a true-peak reading.

## Build

From the repository root, with Python 3.11+ and ffmpeg (libmp3lame, aac, libx264):

```bash
python3 tools/build_pack.py
python3 -m http.server 43207
```

The page is static. It is served with Python's HTTP server so the MIDI and media keep working relative paths. There is no application server and no package install. Standard library only.

`build/` holds the intermediate WAV, the procedural PPM, and the film plate. Those files are gitignored. The delivered audio is the MP3.

## Checks the validator actually runs

File existence, parse, PPQ, tempo, 4/4, end-of-track boundary, note pairing, ranges, monophonic bass, motif, and sequence, harmonic keys and pad polyphony cap of four, the drum map on channel 10, note-off before note-on at a shared tick, absence of program changes and other channel messages, departure flags against the declared pitch-class set, agreement with the canonical score, and agreement between each arrangement and the placed part files. The open section must be thinner and must contain no drums, bass, or motif. The return must restate motif A. Motif and sequence must not overlap in a section. Motif A contours must differ across kits. Arrangement track count is taken from that arrangement spec. Core variations must differ in start, pitch, and duration, and variation A attack tuples must not be shared across kits. A negative overlap fixture is written outside the pack and must be rejected.

## Drafts and publication

Social captions, the X post, and the Medium article are drafts. They are not access controls. If this repository is public, the drafts are public. Do not treat them as posted to Instagram, X, or Medium.

Prepared repository description: Original note-only Balearic Trance construction kits, with matched validation and a simple-synth preview.

Prepared topics: midi, balearic-trance, trance, music-production, composition.

No release tag was created. `index.html` keeps its name because players and links depend on it. This page is the file catalog the pack requires.

## Limitations

Variation A is the theme set. Variation B changes the part. The sequence section places sequence A with drums, bass, keys, and pad while the motif is silent. The open section uses keys, a sparse sequence, and pad only. The return uses the same motif A file as the theme. Do not stack a part file on the arrangement. The primary MP3 is bars 17-32 of kit 01, an excerpt of the longer arrangement, not a master. These parts are original. Balearic is a broad creative label here, not a place claim.
