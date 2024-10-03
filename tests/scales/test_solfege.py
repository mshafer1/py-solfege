import pytest

import solfege


@pytest.mark.parametrize(
    "starting_note, scale_type, note, expected",
    [
        ("C", solfege.ScaleType.MAJOR, "C", "Do"),
        ("F", solfege.ScaleType.MAJOR, "E", "Ti"),
        ("C", solfege.ScaleType.MAJOR, "C#", "Di"),
        ("C", solfege.ScaleType.MAJOR, "Db", "Ra"),
        ("Bb", solfege.ScaleType.MAJOR, "B", "Di"),
        ("Bb", solfege.ScaleType.MAJOR, "Eb", "Fa"),
        ("Bb", solfege.ScaleType.MAJOR, "E", "Fi"),
        ("C", solfege.ScaleType.MAJOR, "E", "Mi"),
        ("C", solfege.ScaleType.MAJOR, "Eb", "Me"),
        ("C", solfege.ScaleType.MAJOR, "D#", "Ri"),
        ("C", solfege.ScaleType.MAJOR, "B#", "Do"),
        ("C", solfege.ScaleType.MAJOR, "Cb", "Ti"),
        # full test case - C Major
        ("C", solfege.ScaleType.MAJOR, "C", "Do"),
        ("C", solfege.ScaleType.MAJOR, "C#", "Di"),
        ("C", solfege.ScaleType.MAJOR, "Db", "Ra"),
        ("C", solfege.ScaleType.MAJOR, "D", "Re"),
        ("C", solfege.ScaleType.MAJOR, "D#", "Ri"),
        ("C", solfege.ScaleType.MAJOR, "Eb", "Me"),
        ("C", solfege.ScaleType.MAJOR, "E", "Mi"),
        ("C", solfege.ScaleType.MAJOR, "E#", "Fa"),
        ("C", solfege.ScaleType.MAJOR, "Fb", "Mi"),
        ("C", solfege.ScaleType.MAJOR, "F", "Fa"),
        ("C", solfege.ScaleType.MAJOR, "F#", "Fi"),
        ("C", solfege.ScaleType.MAJOR, "Gb", "Se"),
        ("C", solfege.ScaleType.MAJOR, "G", "Sol"),
        ("C", solfege.ScaleType.MAJOR, "G#", "Si"),
        ("C", solfege.ScaleType.MAJOR, "Ab", "Le"),
        ("C", solfege.ScaleType.MAJOR, "A", "La"),
        ("C", solfege.ScaleType.MAJOR, "A#", "Li"),
        ("C", solfege.ScaleType.MAJOR, "Bb", "Te"),
        ("C", solfege.ScaleType.MAJOR, "B", "Ti"),
        ("C", solfege.ScaleType.MAJOR, "B#", "Do"),
        # full test case, Am
        ("A", solfege.ScaleType.MINOR, "A", "La"),  # 1st
        ("A", solfege.ScaleType.MINOR, "A#", "Li"),
        ("A", solfege.ScaleType.MINOR, "Bb", "Te"),
        ("A", solfege.ScaleType.MINOR, "B", "Ti"),  # 2nd
        ("A", solfege.ScaleType.MINOR, "Cb", "Ti"),
        ("A", solfege.ScaleType.MINOR, "C", "Do"),  # 3rd
        ("A", solfege.ScaleType.MINOR, "C#", "Di"),
        ("A", solfege.ScaleType.MINOR, "Db", "Ra"),
        ("A", solfege.ScaleType.MINOR, "D", "Re"),  # 4th
        ("A", solfege.ScaleType.MINOR, "D#", "Ri"),
        ("A", solfege.ScaleType.MINOR, "Eb", "Me"),
        ("A", solfege.ScaleType.MINOR, "E", "Mi"),  # 5th
        ("A", solfege.ScaleType.MINOR, "E#", "Fa"),
        ("A", solfege.ScaleType.MINOR, "Fb", "Mi"),
        ("A", solfege.ScaleType.MINOR, "F", "Fa"),  # 6th
        ("A", solfege.ScaleType.MINOR, "F#", "Fi"),
        ("A", solfege.ScaleType.MINOR, "Gb", "Se"),
        ("A", solfege.ScaleType.MINOR, "G", "Sol"),  # 7th
        ("A", solfege.ScaleType.MINOR, "G#", "Si"),
        ("A", solfege.ScaleType.MINOR, "Ab", "Le"),  # 8th
    ],
)
def test___starting_note___scale_chromatic_notes___match_expected(
    starting_note, scale_type, note, expected
):
    result = solfege.Scale(solfege.Note(starting_note), scale_type).solfege(solfege.Note(note))

    assert result == expected
