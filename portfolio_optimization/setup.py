from setuptools import setup

setup(name='portfolio_optimization',
	  version='0.0.1',
	  desciption='A portfolio optimization library',
	  long_description='Markowitz Portfolio and its Extension',
	  url='https://github.com/WizardKingZ/portfolio_optimization',
	  author='Johnew Zhang',
	  author_email='johnew.zhang@columbia.edu',
	  license='MIT',
	  packages=['portfolio_optimization'],
	  install_requires=[
          'matplotlib',
          'cvxopt',
          'numpy',
          'pandas',
          'seaborn'
      ]
	  zip_safe=False)
