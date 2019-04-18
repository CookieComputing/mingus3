#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, notes module.
#    Copyright (C) 2008-2009, Bart Spaans
#    Copyright (C) 2011, Carlo Stemberger
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Basic module for notes.

This module is the foundation of the music theory package.

It handles conversions from integers to notes and vice versa and thus
enables simple calculations.
"""

from .mt_exceptions import NoteFormatError, RangeError, FormatError

_NOTE_DICT = {
    'C': 0,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 7,
    'A': 9,
    'B': 11
}
FIFTHS = ['F', 'C', 'G', 'D', 'A', 'E', 'B']


def int_to_note(note_int: int, accidentals: str = '#') -> str:
    """Convert integers in the range of 0-11 to notes in the form of C or C#
    or Db. If not specified, sharps will be used.

    Raises:
        RangeError: If the note_int is not an integer in the range 0-11.
        FormatError: If note is not a valid accidental

    Examples:
    >>> int_to_note(0)
    'C'
    >>> int_to_note(3)
    'D#'
    >>> int_to_note(3, 'b')
    'Eb'
    """
    if note_int not in list(range(12)):
        raise RangeError('int not in range (0-11): {}'.format(note_int))
    notes_sharp = ['C', 'C#', 'D', 'D#', 'E',
                   'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    notes_flat = ['C', 'Db', 'D', 'Eb', 'E',
                  'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
    if accidentals == '#':
        return notes_sharp[note_int]
    elif accidentals == 'b':
        return notes_flat[note_int]
    else:
        raise FormatError("'%s' not valid as accidental" % accidentals)


def is_enharmonic(note1: str, note2: str) -> bool:
    """Test whether note1 and note2 are enharmonic, i.e. they sound the same."""
    return note_to_int(note1) == note_to_int(note2)


def is_valid_note(note: str) -> bool:
    """Return True if note is in a recognised format. False if not."""
    if not note:
        return False
    # the first character of string is valid if it's a
    # capital letter from A - G
    if note[0] not in _NOTE_DICT:
        return False
    # Arbitrary flats and sharps are okay
    return all(post == 'b' or post == '#' for post in note[1:])


def note_to_int(note: str) -> int:
    """Convert notes in the form of C, C#, Cb, C##, etc. to an integer in the
    range of 0-11.

    Throws:
        NoteFormatError: If the note format is not recognised.
    """
    if not is_valid_note(note):
        raise NoteFormatError("Unknown note format '%s'" % note)

    val = _NOTE_DICT[note[0]]
    # Check for '#' and 'b' postfixes
    for post in note[1:]:
        if post == 'b':
            val -= 1
        elif post == '#':
            val += 1
    return val % 12


def reduce_accidentals(note: str) -> str:
    """Reduce any extra accidentals to proper notes.

    Raises:
        NoteFormatError: If the note is improperly formatted

    Example:
    >>> reduce_accidentals('C####')
    'E'
    """
    if not is_valid_note(note):
        raise NoteFormatError("Invalid note: {}".format(note))

    val = note_to_int(note[0])
    for token in note[1:]:
        if token == 'b':
            val -= 1
        elif token == '#':
            val += 1
        else:
            raise NoteFormatError("Unknown note format '{}'".format(note))
    if val >= note_to_int(note[0]):
        return int_to_note(val % 12)
    return int_to_note(val % 12, 'b')


def remove_redundant_accidentals(note: str) -> str:
    """Remove redundant sharps and flats from the given note.

    Examples:
    >>> remove_redundant_accidentals('C##b')
    'C#'
    >>> remove_redundant_accidentals('Eb##b')
    'E'
    """
    if not is_valid_note(note):
        raise NoteFormatError("Invalid note: {}".format(note))

    val = 0
    for token in note[1:]:
        if token == 'b':
            val -= 1
        elif token == '#':
            val += 1
    result = note[0]
    while val > 0:
        result = __augment(result)
        val -= 1
    while val < 0:
        result = __diminish(result)
        val += 1
    return result


def augment(note: str) -> str:
    """Augment a given note.

    Raises:
        NoteFormatError: If the note is invalid

    Examples:
    >>> augment('C')
    'C#'
    >>> augment('Cb')
    'C'
    """
    if not is_valid_note(note):
        raise NoteFormatError("Invalid note: {}".format(note))
    return __augment(note)


def diminish(note: str) -> str:
    """Diminish a given note.

    Examples:
    >>> diminish('C')
    'Cb'
    >>> diminish('C#')
    'C'
    """
    if not is_valid_note(note):
        raise NoteFormatError("Invalid note: {}".format(note))
    return __diminish(note)


def __augment(note):
    """Augment a given note. Ignores any note formatting checking."""
    if note[-1] != 'b':
        return note + '#'
    return note[:-1]


def __diminish(note):
    """Diminish a given note. Ignores any note formatting checking."""
    if note[-1] != '#':
        return note + 'b'
    return note[:-1]
