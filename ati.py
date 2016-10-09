#!/usr/bin/env python
#All credit for binvis goes to Aldo Corseti
#as does the credit for the optparse code, lines 12-59
#which for the sake of convenience were moved from binvis here
#whose Github can be found at https://github.com/cortesi

import scurve
import binvis

#feed audio data to binvis, which will export 
#it to a .png

from optparse import OptionParser, OptionGroup
parser = OptionParser(
            usage = "%prog [options] infile [output]",
            version="%prog 0.1",
        )
parser.add_option(
    "-b", "--block", action="store",
    dest="block", default=None,
    help="Mark a block of data with a specified color. Format: hexstartaddr:hexendaddr[:hexcolor]"
)
parser.add_option(
    "-c", "--color", action="store",
    type="choice", dest="color", default="class",
    choices=["class", "hilbert", "entropy", "gradient"],
    help="Color map."
)
parser.add_option(
    "-m", "--map", action="store",
    type="choice", dest="map", default="hilbert",
    choices=sorted(scurve.curveMap.keys()),
    help="Pixel layout map. Can be any supported curve."
)
parser.add_option(
    "-n", "--namesuffix", action="store",
    type="str", dest="suffix", default="",
    help="Suffix for generated file names. Ignored if destination is specified."
)
parser.add_option(
    "-p", "--progress", action="store_true", default=False,
    dest="progress",
    help="Don't show progress bar - print the destination file name."
)
parser.add_option(
    "-s", "--size", action="store",
    type="int", dest="size", default=256,
    help="Image width in pixels."
)
parser.add_option(
    "-t", "--type", type="choice",
    dest="type", default="unrolled",
    choices=["unrolled", "square"],
    help="Image aspect ratio - square (1x1) or unrolled (1x4)"
)
parser.add_option(
    "-q", "--quiet", action="store_true",
    dest="quiet", default=False
)
options, args = parser.parse_args()

#Assumes all non-option args are audio files
#and runs each of them through binvis.
#THIS MEANS DONT SPECIFY OUTPUT FILES!
#binvis will generate them for you. 
#filenames keeps track of generated .pngs

filenames = []
for x in range (0, len(args)):
    print("Exporting %i of %i" % (x + 1, len(args)))
    filenames.append(binvis.main(options, args[x]))
