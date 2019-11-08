from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='notebook_splitter',
      version='1.5',
      description='Jupyter Notebook Splitter',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/AndiH/notebook-splitter',
      author='Andreas Herten',
      author_email='a.herten@gmail.com',
      license='MIT',
      packages=['nbsplit'],
      zip_safe=False,
      entry_points={
      	'console_scripts': ['notebook-splitter=nbsplit.nbsplit:main']
      	})
