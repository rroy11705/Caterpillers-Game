import sys
from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'compressed': True,
        'packages':['pygame'],
##        'includes': [
##            'RedApple.png','caterpiller_icon.png','caterpiller_head.png','caterpiller_body.png'
##        ],
        'path': sys.path + ['modules']
    }
}

executables = [
    Executable('caterpillers.py')
    
]

setup(name='Carerpillers',
      version='0.1',
      description='Caterpiller eats Apple...and there are some restriction',
      options=options,
      executables=executables
      )
##from distutils.core import setup
##import py2exe
##
##setup(console=['caterpillers.py'])
