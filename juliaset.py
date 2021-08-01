import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

class JuliaSet:

    def __init__(self, size=256, dpi=300):
        """
        Constructor of the JuliaSet class

        :param size: size in pixels (for both width and height)
        :param dpi: dots per inch (default 300)
        """

        # Set parameters
        self.size = size
        self.dpi = dpi

    def run(self, mirror=False, norm=True, show=False, fname='juilaset-output'):
        """
        Run the Julia set generator

        :param mirror: if True the julia is mirrored horizontally and
            vertically; each mirror is concatenate with the original
            to produce a new image
        :param norm: if true the Julia set is normalized by its
            absolute maximum value.
        :param show: if show is `False` th eoutput image will be
            written as a PNG file named `fname`
        :param fname: Name of the output PNG file to write on disk
        """

        # Get a complex value among a list of best Julia sets 
        cpxNum = self.getComplexValue()

        # Get the target area
        # For more randomness, the target area is a random 
        # subset of a wide one defined with x[-1.5, 1.5] and
        # y[-1.5, 1.5]
        xrng, yrng = self.getTargetArea()

        # Process
        julia = self.processJulia(cpxNum, xrng, yrng)

        # Normalization
        if(norm):
            julia /= np.amax(np.abs(julia))

        # Mirroring
        if(mirror):
            # Horizontal mirroring and concatenate
            juliamirror = np.flip(julia, axis=1)
            julia = np.concatenate((julia, juliamirror), axis=1)
            # Vertical mirroring and concatenate
            juliamirror = np.flip(julia, axis=0)
            julia = np.concatenate((julia, juliamirror), axis=0)

        # Plot the output with a random colormap using matplotlib
        self.plotJuliaSet(julia, show=show, fname=fname)

    def getComplexValue(self):
        """
        Random choice in a list of best complex values for Julia 
        sets (real, imag).

        :return cpxNum: a semi-random complex value
        """

        # Define the list of best complex values 
        cpxList = [
            (-0.10, 0.650), (0.00, 0.80), (0.370, 0.100), 
            (0.355, 0.355), (-0.54, 0.54), (0.340, -0.05),
            (0.37, 0.10), (0.355, 0.355)
        ]

        # Randomly choose one
        cpxTmp =  random.choice(cpxList)

        # Manipulate the base value slightly to make it a little more unique
        cpxNum = self.twearkComplex(cpxTmp)

        return cpxNum

    def twearkComplex(self, cpxTmp):
        """
        Manipulate the base value slightly to make it a little more unique.

        :param cpxTmp: complex value to modify
        :param cpxNum: a slightly manipulate version of the input
        """

        # Get the signs for the imaginary parts
        isign = random.randrange(-1, 1, 2)

        # Get a value variation for for real and imaginary parts
        # The possible variation range is fixed at +/- 2% to stay
        # In the neightborhood of the initial value
        rsigma = random.uniform(0.98, 1.02)
        isigma = random.uniform(0.98, 1.02)

        # Apply modification and return the new complex value
        realPart = cpxTmp[0] * rsigma
        imagPart = cpxTmp[1] * isigma * isign

        return complex(realPart, imagPart)

    def getTargetArea(self):
        """
        For more randomness, the target area is a random 
        subset of a wide one defined with x[-1.5, 1.5] and
        y[-1.5, 1.5]

        :return xrng, yrng: tuples containing (xmin, xmax)
            and (ymin, ymax)
        """

        # Randomly choose the center of the target area
        # Possible values are in [-1.0, 1.0] to stay in an
        # area where there are always pieces of fractals
        xctr = random.uniform(-1.0,1.0)
        yctr = random.uniform(-1.0,1.0)

        # Extend around the center
        xrng = (xctr-0.5, xctr+0.5)
        yrng = (yctr-0.5, yctr+0.5)

        return xrng, yrng

    def processJulia(self, cpxNum, xrng, yrng, escrad=3, niter=250):
        """
        Calculate the Julia set for the given input parameters.

        :param cpxNum: complex value acting as a seed for the Julia set
        :param xrng: range of values (min, max) for the x-axis
        :param yrng: range of values (min, max) for the y-axis
        :param escrad: escape radius
        :param niter: maximum number of iterations
        """

        # Initialize numpy array of dimensions (size, size) with zeros
        julia = np.zeros((self.size, self.size), dtype=np.float32)

        # Calculate the width (equal to height) of the image since the
        # image is defined as a square
        width = xrng[1] - xrng[0]  # xmax - xmin = ymax - ymin

        # Randomly choose the sign of the shade
        #ssign = random.randrange(-1, 1, 2)
        ssign = -1.

        # Loop over x range
        for ix in range(self.size):
            # Get the pixel position in the complex plane
            # For the real part
            realPart = float(ix) / self.size * width + xrng[0]

            # Loop over y range
            for iy in range(self.size):
                # Get the pixel position in the complex plane
                # For the imaginary part
                imagPart = float(iy) / self.size * width + yrng[0]

                # Build the complex
                cpxTmp = complex(realPart, imagPart)

                # Initialize iteration counter
                it = 0

                # Loop over iterations
                while(np.abs(cpxTmp) <= escrad**2 and it < niter):
                    # Quadratic polynomial
                    cpxTmp = cpxTmp**2 + cpxNum
                    # Increment iteration counter
                    it += 1
                
                # Calculate the shade (a cool thing find somewhere on the net)
                shade = 1. - np.sqrt(it/niter)

                # Fill the outpout array
                julia[ix][iy] = ssign * shade

        return julia

    def plotJuliaSet(self, julia, fname='juilaset-output', show=False):
        """
        Plot the output Julia set and show it in matplotlib window or
        write it on disk as a png file.

        :param julia: the Julia set
        :param show: if show is `False` th eoutput image will be
            written as a PNG file named `fname`
        :param fname: Name of the output PNG file to write on disk
        """

        # List of beautiful colormap for Julia sets
        cmapList = [
            cm.Blues, cm.Greens, cm.Purples, cm.hot, cm.inferno, 
            cm.binary, cm.rainbow, cm.twilight_shifted, cm.plasma
        ]

        # Randomly chose one colormap
        cmapName = random.choice(cmapList)

        # Plot the image with a gaussian interpolation
        fig = plt.gcf()
        plt.imshow(julia, interpolation='gaussian', cmap=cmapName)
        
        # Disable axis
        plt.axis('off')

        if(show):
            plt.show()
        else:
            # Write on disk
            fig.savefig(fname+".png", pad_inches=0.05, bbox_inches='tight')

if __name__ == "__main__":
    # execute only if run as a script
    genJuliaSet = JuliaSet()
    genJuliaSet.run()
