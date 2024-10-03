import pytest

import solfege


@pytest.mark.parametrize(
    "starting_note, scale_type, expected_notes",
    [
        (
            "C#",
            solfege.ScaleType.MAJOR,
            ["C#", "D#", "E#", "F#", "G#", "A#", "B#", "C#"],
        ),
        (
            "F#",
            solfege.ScaleType.MAJOR,
            ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"],
        ),
        ("B", solfege.ScaleType.MAJOR, ["B", "C#", "D#", "E", "F#", "G#", "A#", "B"]),
        ("E", solfege.ScaleType.MAJOR, ["E", "F#", "G#", "A", "B", "C#", "D#", "E"]),
        ("A", solfege.ScaleType.MAJOR, ["A", "B", "C#", "D", "E", "F#", "G#", "A"]),
        ("D", solfege.ScaleType.MAJOR, ["D", "E", "F#", "G", "A", "B", "C#", "D"]),
        ("G", solfege.ScaleType.MAJOR, ["G", "A", "B", "C", "D", "E", "F#", "G"]),
        ("C", solfege.ScaleType.MAJOR, ["C", "D", "E", "F", "G", "A", "B", "C"]),
        ("F", solfege.ScaleType.MAJOR, ["F", "G", "A", "Bb", "C", "D", "E", "F"]),
        ("Bb", solfege.ScaleType.MAJOR, ["Bb", "C", "D", "Eb", "F", "G", "A", "Bb"]),
        ("Eb", solfege.ScaleType.MAJOR, ["Eb", "F", "G", "Ab", "Bb", "C", "D", "Eb"]),
    ],
)
def test___starting_note___scale_chromatic_notes___match_expected(
    starting_note, scale_type, expected_notes
):
    note = solfege.Note(starting_note)

    result = solfege.Scale(note, scale_type)

    assert len(result._diatonic_notes) == 8
    assert [note_.name for note_ in result._diatonic_notes] == expected_notes
