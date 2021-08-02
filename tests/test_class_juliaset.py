import unittest
import random
import os
from juliaset import JuliaSet

class TestJuliaSet(unittest.TestCase):

    def test_initialize(self):

        # Initialize a JuliaSet instance
        juliaInstance = JuliaSet()

        self.assertEqual(juliaInstance.size, 256)
        self.assertEqual(juliaInstance.dpi, 300)
        self.assertEqual(juliaInstance.norm, True)
        self.assertEqual(juliaInstance.mirror, False)
        self.assertEqual(juliaInstance.escrad, 3)
        self.assertEqual(juliaInstance.niter, 250)

    def test_param_valid_keys(self):

        # Initialize a JuliaSet instance
        juliaInstance = JuliaSet()

        # Call param function
        juliaInstance.param(
            size=128, dpi=600, norm=False, mirror=True,
            escrad=4, niter=500
        )

        self.assertEqual(juliaInstance.size, 128)
        self.assertEqual(juliaInstance.dpi, 600)
        self.assertEqual(juliaInstance.norm, False)
        self.assertEqual(juliaInstance.mirror, True)
        self.assertEqual(juliaInstance.escrad, 4)
        self.assertEqual(juliaInstance.niter, 500)

    def test_twearkComplex(self):

        # Initialize a JuliaSet instance
        juliaInstance = JuliaSet()

        cpxTmp = (1., 1.)
        cpxNum = juliaInstance.twearkComplex(cpxTmp)

        self.assertTrue(cpxNum.real >= 0.98 and cpxNum.real <= 1.02)
        self.assertTrue(abs(cpxNum.imag) >= 0.98 and abs(cpxNum.imag) <= 1.02 )
    
    def test_getComplexValue(self):

        # Initialize random seed
        random.seed(0)

        # Initialize a JuliaSet instance
        juliaInstance = JuliaSet()

        cpxNum = juliaInstance.getComplexValue()

        self.assertAlmostEqual(cpxNum, complex(0.36319, -0.101861), delta=1.e-5)

    def test_getTargetArea(self):

        # Initialize a JuliaSet instance
        juliaInstance = JuliaSet()

        xrng, yrng = juliaInstance.getTargetArea()

        self.assertTrue(xrng[0] >= -1.5 and xrng[0] <= 1.0)
        self.assertTrue(xrng[1] >= -1.0 and xrng[1] <= 1.5)
        self.assertTrue(yrng[0] >= -1.5 and yrng[0] <= 1.0)
        self.assertTrue(yrng[1] >= -1.0 and yrng[1] <= 1.5)
        
        self.assertTrue(xrng[1]-xrng[0] == 1.)
        self.assertTrue(yrng[1]-yrng[0] == 1.)

    def test_processJulia(self):

        # Initialize random seed
        random.seed(0)

        # Initialize a JuliaSet instance
        juliaInstance = JuliaSet()

        # Call param function and fix size at 8 for small test
        juliaInstance.param(
            size=8, dpi=600, norm=False, mirror=False,
            escrad=4, niter=500
        )

        # Fix cpxNum, xrng and yrng
        cpxNum = complex(1.0, 1.0)
        xrng = (-0.5, 0.5)
        yrng = (-0.5, 0.5)

        # call the function
        julia = juliaInstance.processJulia(cpxNum, xrng, yrng)

        attemptOutput = [
            [-0.91055727, -0.91055727, -0.9225403, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727],
            [-0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727],
            [-0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727],
            [-0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727],
            [-0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727],
            [-0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727],
            [-0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727],
            [-0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727, -0.91055727]
        ]

        for i in range(8):
            for j in range(8):
                self.assertAlmostEqual(julia[i][j], attemptOutput[i][j], delta=1.e-5)
        