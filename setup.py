from setuptools import setup


setup(name='sphereob',
      version='0.0.82',
      description='GUI program to model the airborne EM response of a sphere underlying conductive overburden',
      url='https://github.com/adzamper71/SPHEREOB',
      author='Anthony Zamperoni',
      author_email='azamperoni@laurentian.ca',
      packages=['sphereob',
                'sphereob.GUI',
                'sphereob.utils',
                'sphereob.resources'],
      long_description=open('readme.rst').read(),
      scripts=[],
      entry_points={'console_scripts': ['sphereob = sphereob.GUI.sphere_overburden_gui:main']},
      install_requires=['numpy',
                        'pandas',
                        'matplotlib',
                        'qdarkstyle',
                        'quadpy',
                        'pyqt5'],
      include_package_data=True)
