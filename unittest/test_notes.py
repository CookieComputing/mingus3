#!/usr/bin/python
# -*- coding: utf-8 -*-
import mingus.core.notes as notes
from mingus.core.mt_exceptions import RangeError, NoteFormatError
import unittest


class TestNotes(unittest.TestCase):
    def setUp(self):
        self.base_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.sharps = [x + '#' for x in self.base_notes]
        self.flats = [x + 'b' for x in self.base_notes]
        self.exotic = [x + 'b###b#' for x in self.base_notes]

    def test_base_note_validity(self):
        list(map(
            lambda x: self.assertTrue(notes.is_valid_note(x), 'Base notes A-G'),
            self.base_notes))

    def test_sharp_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x),
                                           'Sharp notes A#-G#'), self.sharps))

    def test_flat_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x),
                                           'Flat notes Ab-Gb'),
                 self.flats))

    def test_exotic_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x),
                                           'Exotic notes Ab##b#-Gb###b#'),
                 self.exotic))

    def test_excessive_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x),
                                           "Redundant but valid notes"),
                 ["B#####bbbb##", "C##bbb##", "F#########", "Abbbbbbb"]))

    def test_faulty_note_invalidity(self):
        list(map(lambda x: self.assertFalse(notes.is_valid_note(x),
                                            'Faulty notes'),
                 ['asdasd', 'C###f', 'c', 'd', 'E*', 'b', 'cb', 'c#']))

    def test_empty_note_invalidity(self):
        self.assertFalse(notes.is_valid_note(""), "Empty string invalid note")

    def test_int_to_note(self):
        known = {
            (0, '#'): 'C',
            (3, '#'): 'D#',
            (8, '#'): 'G#',
            (11, '#'): 'B',
            (0, 'b'): 'C',
            (3, 'b'): 'Eb',
            (8, 'b'): 'Ab',
            (11, 'b'): 'B'
        }
        for k in list(known.keys()):
            self.assertEqual(known[k], notes.int_to_note(k[0], k[1]),
                             '{known_int} with {accidental} not corresponding '
                             'to {result_note}, expecting {known_note}'.
                             format(known_int=k[0],
                                    accidental=k[1],
                                    result_note=notes.int_to_note(k[0], k[1]),
                                    known_note=known[k]))

    def test_invalid_int_to_note(self):
        faulty = [-1, 12, 13, 123123, -123, 0.5, 11.1, 1.5, 5.5]
        list(map(lambda x: self.assertRaises(RangeError, notes.int_to_note, x),
                 faulty))

    def test_reduce_accidentals(self):
        known = {
            'C': 'C',
            'F#': 'F#',
            'Bb': 'Bb',
            'G##': 'A',
            'Abb': 'G',
            'B##': 'C#',
            'C####': 'E',
            'C#b#b#b#b': 'C',
            'C#####bbbb': 'C#'
        }
        for k in list(known.keys()):
            self.assertEqual(known[k], notes.reduce_accidentals(k),
                             'The reduced note of {key} is not {result_note}, '
                             'expecting {correct_note}'.format(
                                 key=k,
                                 result_note=notes.reduce_accidentals(k),
                                 correct_note=known[k]))

    def test_reduce_accidentals_bad_note(self):
        bad_notes = ['', 'cb', '?', 'Baw', 'B##B', 'Abb#b#zb#b']
        list(map(lambda x:
                 self.assertRaises(NoteFormatError,
                                   notes.remove_redundant_accidentals,
                                   x),
                 bad_notes))

    def test_remove_redundant_accidentals(self):
        known = {
            'C##b': 'C#',
            'Eb##b': 'E'
        }
        for k in list(known.keys()):
            self.assertEqual(known[k], notes.remove_redundant_accidentals(k),
                             'The simplified note of {key} is not '
                             '{result}, expecting {correct_note}'.format(
                                 key=k,
                                 result=notes.remove_redundant_accidentals(k),
                                 correct_note=known[k]))

    def test_remove_redundant_accidentals_bad_note(self):
        bad_notes = ['', 'cb', '?', 'Baw', 'B##B', 'Abb#b#zb#b']
        list(map(lambda x:
                 self.assertRaises(NoteFormatError,
                                   notes.remove_redundant_accidentals,
                                   x),
                 bad_notes))

    def test_augment(self):
        known = {
            'C': 'C#',
            'C#': 'C##',
            'Cb': 'C',
            'Cbb': 'Cb'
        }
        list(map(lambda x:
                 self.assertEqual(known[x], notes.augment(x),
                                  'The augmented note of {note} is not '
                                  '{result}, expecting {correct_note}'.format(
                                      note=x,
                                      result=notes.augment(x),
                                      correct_note=known[x])),
                 list(known.keys())))

    def test_bad_augment(self):
        bad_notes = ['', 'cb', '?', 'Baw', 'B##B', 'Abb#b#zb#b']
        list(map(lambda x:
                 self.assertRaises(NoteFormatError, notes.augment, x),
                 bad_notes))

    def test_diminish(self):
        known = {
            'C': 'Cb',
            'C#': 'C',
            'C##': 'C#',
            'Cb': 'Cbb'
        }
        list(map(lambda x:
                 self.assertEqual(known[x], notes.diminish(x),
                                  'The diminished note of {note} is not '
                                  '{result}, expecting {correct_note}'.format(
                                      note=x,
                                      result=notes.diminish(x),
                                      correct_note=known[x])),
                 list(known.keys())))

    def test_bad_diminish(self):
        bad_notes = ['', 'cb', '?', 'Baw', 'B##B', 'Abb#b#zb#b']
        list(map(lambda x:
                 self.assertRaises(NoteFormatError, notes.diminish, x),
                 bad_notes))

    def test_enharmonic(self):
        enharmonic_notes = [('B#', 'C'), ('Ab', 'G#'), ('Cb', 'B'), ('F', 'E#'),
                            ('D', 'D'), ('Eb', 'D#')]
        map(lambda x, y:
            self.assertTrue(notes.is_enharmonic(x, y),
                            "{first_note} and {second_note} are supposed to be "
                            "enharmonic".format(first_note=x, second_note=y)),
            enharmonic_notes)

    def test_complex_reduction_enharmonic(self):
        self.assertTrue(
            notes.is_enharmonic(notes.reduce_accidentals("C###bbbb"),
                                notes.reduce_accidentals("B#b#b#b#b")))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestNotes)
