from setuptools import setup

setup(name='notebook_splitter',
      version='1.1',
      description='Jupyter Notebook Splitter',
      url='https://github.com/AndiH/notebook-splitter',
      author='Andreas Herten',
      author_email='a.herten@gmail.com',
      license='MIT',
      packages=['nbsplit'],
      zip_safe=False,
      entry_points={
      	'console_scripts': ['notebook-splitter=nbsplit.nbsplit:main']
      	})
