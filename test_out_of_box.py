#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, sys

#...for parsing the arguments.
import argparse

#...for the logging.
import logging as lg

#...for the unit testing.
import unittest

#...for the files.
import glob

# The Out-of-the-Box contents.
from data.ootb import ootb_contents


class OutOfBoxTest(unittest.TestCase):

    POSSUM_OUTPUT = "/tmp/simdir"

    def setUp(self):
        self.data = ootb_contents

    def tearDown(self):
        pass

    def test_output_contents(self):

        ## The files in the output directory.

        ## The full paths of the POSSUM output directory's contents.
        contents_full_path = glob.glob(OutOfBoxTest.POSSUM_OUTPUT + "*")

        ## The full paths of the directories.
        dirs = [ x for x in contents_full_path if os.path.isdir(x) ]

        ## The full paths of the files.
        files = [ x for x in contents_full_path if os.path.isfile(x) ]

        ## The basenames.
        contents = sorted([ os.path.basename(x) for x in contents_full_path ])

        # Update the logs.
        for x in dirs:
            lg.info(" * Found directory : '%s'" % (x))
        lg.info(" *")
        #
        for x in files:
            lg.info(" * Found file      : '%s'" % (x))
        lg.info(" *")

        # Check the number of entries in the POSSUM output directory.
        self.assertEqual(len(contents), 21)
        #
        self.assertEqual(len(dirs), 1)
        #
        self.assertEqual(len(files), 20)

        # Check the contents of each file.

        #
        # The original brain model.
        #

        ## Path to the (copy of the) original brain model.
        brain_model_path = os.path.join(OutOfBoxTest.POSSUM_OUTPUT, "brain.nii.gz")

        ## The file size of the (copy of the) brain model [bytes].
        brain_model_file_size = os.path.getsize(brain_model_path)
        #
        self.assertEqual(brain_model_file_size, 7949764)


if __name__ == "__main__":

    lg.basicConfig(filename='testoutput/log_test_out_of_box.log', filemode='w', level=lg.DEBUG)

    ## The path to the POSSUM output directory.
    possum_output_path = OutOfBoxTest.POSSUM_OUTPUT
    #
    if len(sys.argv) > 1:
        OutOfBoxTest.POSSUM_OUTPUT = sys.argv.pop()
    #
    if not os.path.isdir(OutOfBoxTest.POSSUM_OUTPUT):
        raise IOError("* ERROR: Unable to find the POSSUM output directory at '%s'." % (OutOfBoxTest.POSSUM_OUTPUT))


    lg.info(" *")
    lg.info(" *=======================================")
    lg.info(" * Logger output from test_out_of_box.py ")
    lg.info(" *=======================================")
    lg.info(" *")
    lg.info(" * Checking output found in : '%s'" % (possum_output_path))
    lg.info(" *")

    unittest.main()
