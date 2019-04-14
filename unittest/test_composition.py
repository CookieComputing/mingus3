#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

sys.path += ['../']
import unittest


class test_Composition(unittest.TestCase):

    def setUp(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_Composition)
