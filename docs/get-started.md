## Installation
To install,
```bash
pip install git+https://github.com/OpenQuantumDesign/equilux.git
```

Or clone the repository locally and install with:

```bash
git clone https://github.com/OpenQuantumDesign/equilux
pip install .
```

## Documentation

Documentation is implemented with [MkDocs](https://www.mkdocs.org/) and can be read from the [docs](https://github.com/OpenQuantumDesign/midstack/tree/main/docs) folder.

To install the dependencies for documentation, run:

```
pip install -e ".[docs]"
```

To deploy the documentation server locally:

```
cp -r examples/ docs/examples/
mkdocs serve
```
