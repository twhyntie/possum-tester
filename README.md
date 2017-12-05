# POSSUM Testing

Unit tests for running POSSUM.

## Out-of-the-Box Ouput
To test how your system is running on the Out-of-the-Box example provided with
POSSUM (a single slice EPI image), run POSSUM in a `$TESTDIR` and then tun the
Out-of-the-Box unit test provided:

```bash
$ mkdir $TESTDIR
$ cd $TESTDIR
$ Possum
[Press 'Go' on the GUI, let it run, then quit the GUI.]
$ cd $WORKINGDIR
$ python test_out_of_box.py $TESTDIR/simdir
```


## Useful links

* [POSSUM on the FSL Wiki](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/POSSUM/)
* [The POSSUM User Guide](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/POSSUM/UserGuide)
