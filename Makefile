
.PHONY: clean docs docs-setup

clean:
	rm -rf *.pyc __pycache__/
	rm -rf docs/

docs-setup:
	sphinx-quickstart --sep -p add_mult -a "Toru Tamaki" -r 0.1 --ext-autodoc -l en --extensions sphinx.ext.napoleon docs/
	patch -p0 < conf.py.diff
docs:
	sphinx-apidoc -f -o docs/source/ ./
	sphinx-build -b html docs/source docs/build/html

