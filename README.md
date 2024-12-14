# aidge_wheels

Python pre-compiled wheels for Aidge packages.

## wheel name convention:

The wheel filename is {distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl.

- distribution

    Distribution name, e.g. ‘django’, ‘pyramid’.

- version

    Distribution version, e.g. 1.0.

- build tag

    Optional build number. Must start with a digit. A tie breaker if two wheels have the same version. Sort as the empty string if unspecified, else sort the initial digits as a number, and the remainder lexicographically.

- language implementation and version tag

    E.g. ‘py27’, ‘py2’, ‘py3’.

- abi tag

    E.g. ‘cp33m’, ‘abi3’, ‘none’.

- platform tag

    E.g. ‘linux_x86_64’, ‘any’. 