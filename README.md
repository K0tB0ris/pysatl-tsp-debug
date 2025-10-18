# PySATL-TSP-DEBUG

## Installation

### Configure Python for debugging

1) Replace "NAME" before running

```bash
cd /tmp/
wget https://www.python.org/ftp/python/3.12.12/Python-3.12.12.tgz
tar xzf Python-3.12.12.tgz
cd Python-3.12.12

./configure --prefix=NAME --enable-pystats --without-pymalloc --with-pydebug --with-address-sanitizer --with-undefined-behavior-sanitizer
make -j $(nproc)
make altinstall
sudo rm /tmp/Python-3.12.12.tgz

NAME/bin/python3.12 -m pip install --upgrade pip setuptools wheel
```

2) Clone the PySATL-TSP fork:

```bash
git clone https://github.com/K0tB0ris/pysatl-tsp.git
cd pysatl-tsp
```

3) Install dependencies for PySATL-TSP:

```bash
poetry install --with dev
poetry build
```

4) Install library

```bash
NAME/bin/python3.12 -m pip install /dist/pysatl_tsp-0.1.0-cp312-cp312-manylinux_2_39_x86_64.whl
NAME/bin/python3.12 -m pip install websockets
```


### Clone the repository

```bash
git clone https://github.com/K0tB0ris/pysatl-tsp-debug.git
```

## Problems

Import CFFI functions memory leak
[Example1](src/example.py)
[Log for Example1](src/res_example.txt)

Memory leak than using C handlers in a pipeline

[pipeline1](src/pipe1.py)
[Log for Example1](src/res_pipe1.txt)

[pipeline2](src/pipe2.py)
[Log for Example1](src/res_pipe1.txt)



