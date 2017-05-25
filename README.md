# theia
`theia` is a 3D Gaussian optics simulation program and library, with support for various optical components, non-sequential tracing, and general astigmatism. It was developed by the Optics Group of the Virgo collaboration at EGO in Cascina, Italy.

`theia` is written in Python2.7, in order to offer full modularity, portability and the object-oriented programming style to users.

In its executable form, `theia` allows for readily written text-based input of the optical setup and clear output of the physical data on the propagation of Gaussian beams, also in text form. When used in its library form, `theia` exploits the scripting possibilities of Python and can be used as a powerful tool for tasks such as optical bench design and optimization, stray light hunting, component alignment, etc.

## Installing
##### Requirements
Building `theia` and its documentation requires a small number of Python and latex packages which are listed in the REQUIREMENTS file.

##### Programs - Documentation
Once in the project root directory, issue the following to install `theia` in your local environment and compile the documentation:
`make install`

To compile just the documentation, issue:
`make go-doc`

To just install `theia` in your local environment:
`make go`

You can then move the pdf documents found in `doc/` and the tutorial files found in `tutos/` to wherever you feel is best and get rid of the project directory if you like.

For a system-wide installation, issue the following with root privileges:
`python setup.py install`

##### Uninstalling
To remove a local `theia` installation from your system, `cd` to the `theia` root repository wherever it is (or download a new one) and issue:
`make clear`

To remove a system wide installation is generally a system-specific procedure but the Python2.7 libraries are generally kept in `/usr/local/lib/python2.7/*-packages`

## Usage
##### `theia` program
In general:
`theia [options] FNAME`

`theia` takes a `.tia` formatted input text file for the optical setup configuration and has a number of options concerning the output of information to the console and the writing of the output text file.

For the format of the input file, see the `userguide.pdf` in `doc/` and for details on the command line options, you can also see the output of `theia -h`.

##### `theia` library
As usual, you can use the
```python
from theia.running.simulation import Simulation
```
idiom from Python to use specific functions or modules from the `theia` library. Please refer to the `userguide.pdf` file for more details on the API.

## Licensing
In the effort of taking down walls in the way of physics and computation, `theia` is free software and is released under the GNU General Public License, version 3+. So please feel free (as in freedom) to copy, take home, modify, teach, learn, and redistribute `theia`.

See the LICENSE file it the project root directory for more details.

## Contributing
`theia` is also open source software, so please feel inventive and contact `raphael.duque@polytechnique.edu` for suggestions, comments, access to the git repository and bug reporting.

## Acknowledgements
This work owes a great deal to many people in and out of the gravitational interferometry community. We would like to thank H.Yamamoto, P. Ehrens, O. Miyakawa, Y. Aso, S. Anderson, G. Duque among others.
