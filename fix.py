import nbformat

path = "llms_deepseek.ipynb"
nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)

if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

nbformat.write(nb, path)
print("Notebook fixed.")