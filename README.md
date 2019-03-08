# Jupyter Notebook Splitter

This tool splits a Jupyter Notebook into Sub-Notebooks depending on cell metadata. It converts a *Master* Notebook into a *Teacher* Notebook and a *Student* Notebook; or into a *Slides* Notebook, a *Tasks* Notebook, and a *Solutions* Notebook.

## Installation

Although the Notebook Splitter is only a single file it can be installed via `pip`

```bash
pip install notebook-splitter
```

## Usage

### Overview

**TL;DR: See `notebook-splitter --help`.**

1. Add [cell metadata](https://ipython.org/ipython-doc/3/notebook/nbformat.html#cell-metadata) to your Jupyter Notebook: Add an `exercise` key (default, can be changed) to the metadata (JSON); give it values (*tags*) on which to create Sub-Notebooks

    ```json
    {
        "exercise": "task"
    }
    // another cell
    {
        "exercise": "solution"
    }
    ```

2. Use `--keep` and `--remove` flags of the Notebook Splitter to keep and remove cells with according *tags*; export it to the respective Notebook:

    ```bash
    notebook-splitter input.ipynb --keep task --remove solution   -o tasks.ipynb
    notebook-splitter input.ipynb --keep solution --remove task   -o solutions.ipynb
    notebook-splitter input.ipynb --remove task --remove solution -o slides.ipynb
    ```

### Examples in Action

See the `examples` directory in this repository.

### Options

* **Repeated Parameters**: `--keep` and `--remove` parameters on the command line of the script can be given multiple times: `--keep task --keep onlytask --remove solution`
* **Remove *All***: As a special parameter value, `--remove all` will remove *all* cells except those for which a `--keep` value is specified (*`--keep all`* is the default)
* **Stdin/Stdout**: If no output file is given with `-o`/`--output`, the resulting Notebook will be printed to `stdout`; if no input file as a parameter is given, the input Notebook will be read from `stdin` (good for Linux-like daisy-chaining of tools)
* **Change *Basekey***: In the above example, the cell meta data key of discrimination is `exercise` which is the default. With `--basekey`, this can be changed.

### Limitations

The values to the `--keep` and `--remove` parameters create sets of values to keep and remove. One could implement this tool probably quite cleverly with set operations (with the added complication of the `--remove all` ). If you can, feel free to file a merge request!
