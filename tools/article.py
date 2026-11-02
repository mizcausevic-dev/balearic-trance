"""Factual article draft. Not published."""

from __future__ import annotations

from tools.statements import AUDITION, ON_PICTURE, PREVIEW_LINE, PROGRAM, PUBLICATION, WARNING

TITLE = "Balearic Trance is a note-only MIDI construction kit"
SUBTITLE = "Four open kits, chord names taken from the keys, and a motif the return restates. The preview is an excerpt, not a master"
TAGS = ["midi", "balearic trance", "trance", "music production", "composition"]
TAG_LINE = "Tags: " + ", ".join(TAGS)


def paragraphs(catalog: dict) -> list[str]:
    kits = catalog["kits"]
    tempos = ", ".join(str(kit["bpm"]) for kit in kits)
    names = ", ".join(f"{kit['title']} in {kit['collection_name']}" for kit in kits)
    chord_lines = " ".join(line for kit in kits for line in kit["chord_lines"])
    theme_lines = " ".join(kit["theme_line"] for kit in kits)
    bass_lines = " ".join(kit["bass_line"] for kit in kits)
    departures = " ".join(item for kit in kits for item in kit["departures"])
    excerpt = catalog["preview_excerpt"]
    return [
        "DRAFT. " + PUBLICATION,
        TAG_LINE,
        "The pack is four coordinated kits in 4/4. Tempos are "
        + tempos
        + " BPM, one fixed integer per kit, inside the 125 to 138 range used for this project. Each kit has six core parts: drums, bass, harmonic keys, motif, sequence, and pad. Every core part has two variations. That is 48 files. There is no reference-only count. Part files are 8 bars. Each kit also has one 32-bar arrangement.",
        "The kits are "
        + names
        + ". "
        + theme_lines
        + " The motif themes are different melodies. They are not transpositions of one line with the same velocities. Variation B of each part changes start times, pitches, and durations. Velocity alone is not the difference.",
        "Each arrangement has four 8-bar sections. Bars 1-8 state the theme: drums, bass, harmonic keys, motif, and pad, with the sequence silent. Bars 9-16 develop the sequence over drums, bass, keys, and pad. The motif does not play in that section. Bars 17-24 are the open section: harmonic keys, a sparse sequence, and a pad, with no drums, no bass, and no motif. Bars 25-32 are the return. The return places the same motif A part as the theme, with the same drums, bass, keys, and pad. The motif is restated. It is not a new tune.",
        chord_lines,
        bass_lines,
        "Bass, motif, and sequence are monophonic. Harmonic keys and the pad may hold four notes. Drums are GM channel 10, MIDI channel index 9, with an explicit map: 36 kick, 37 side stick, 38 acoustic snare, 39 clap, 40 electric snare, 42 closed hat, 46 open hat, 49 crash. C4 is 60. The resolution is 960 ticks per quarter note. Offsets are 0. Seeds name the kits. Nothing is random. "
        + departures,
        PROGRAM,
        "Balearic is a broad creative label in this pack. It is not a claim about a place or a scene. Filter motion and chorus width are not note-only MIDI properties. They are not in these files. The preview synth is a simple-synth: a short kick, noise for hats and snare, a dull saw for the bass, a soft tone for the harmonic keys, a triangle for the sequence, a sine for the motif, and a slow tone for the pad. That mapping is documented. It is not a program change.",
        "The primary preview is an excerpt of the 32-bar Salt Terrace arrangement, bars 17-32, at 128 BPM. "
        + excerpt["reason"]
        + " "
        + PREVIEW_LINE
        + ". The film takes its audio from that preview file and shows the words "
        + ON_PICTURE
        + " on the picture and in the WebVTT captions.",
        AUDITION
        + " The validator reopened the MIDI bytes and compared them with the canonical score. Chord names and the motif intervals were checked against those pitches. That is a structural check. The sample peak written beside the preview is the peak of the integer mix. It is not a loudness figure and it is not a true-peak reading. Nothing in this build is claimed as a master.",
        "The stills are procedural illustrations of a low horizon, three short strokes, and a wide gap. The strokes are the motif. The gap is the open section. They are not photographs of a session or of performers.",
        "When a public URL exists, use either the combined arrangement or the separate parts. " + WARNING,
        "Call to action: the MIDI, the matched report, and the preview belong together. Do not publish this draft to Medium, Instagram, or X from the draft files alone.",
    ]


def markdown(catalog: dict) -> str:
    body = "\n\n".join(paragraphs(catalog))
    return f"# {TITLE}\n\n{SUBTITLE}\n\n{body}\n"


def plain_text(catalog: dict) -> str:
    lines = [TITLE, "", SUBTITLE, "", *paragraphs(catalog), ""]
    return "\n".join(lines) + "\n"
