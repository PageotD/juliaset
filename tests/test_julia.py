import unittest
import random
import os
from juliaset import julia

class TestJuliaSet(unittest.TestCase):

    def test_julia_default_param(self):

        # Initialize a JuliaSet instance
        newset = julia()

        self.assertEqual(newset.size, 256)
        self.assertEqual(newset.dpi, 300)
        self.assertEqual(newset.norm, True)
        self.assertEqual(newset.mirror, False)
        self.assertEqual(newset.escrad, 3)
        self.assertEqual(newset.niter, 250)

    def test_julia_custom_param(self):

        # Initialize a JuliaSet instance
        newset = julia(size=128, dpi=600, norm=False, mirror=True,
            escrad=4, niter=500)

        self.assertEqual(newset.size, 128)
        self.assertEqual(newset.dpi, 600)
        self.assertEqual(newset.norm, False)
        self.assertEqual(newset.mirror, True)
        self.assertEqual(newset.escrad, 4)
        self.assertEqual(newset.niter, 500)