# -*- coding: <UTF-8> -*-
from cx_Freeze import setup, Executable
 
setup(name='teste',
    version='1.0',
    description='teste',
    options={'build_exe': {'packages': ['matplotlib']}},
    executables = [Executable(
                   script='sorteio.py',
                   base=None,
                   icon='icone.ico'
                   )
                  ]
)