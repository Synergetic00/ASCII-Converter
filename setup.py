from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ascii-conv',
  version='0.1.1',
  description='Convert text to be ASCII compatiable and back',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  url='',  
  author='Synergetic00',
  license='GPLv3', 
  classifiers=classifiers,
  keywords='ascii', 
  packages=find_packages(),
  install_requires=[''] 
)