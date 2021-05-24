#
# conftest.py
#

import sys
from os.path import dirname, abspath


#
# Adiciona a raiz do sistema para o path do app - python
# assim o pytest encontra os pacotes e módulos importados nos testes e no app
#
# fonte:
# https://stackoverflow.com/questions/42996270/change-pytest-rootdir#43003192
#

root_dir = dirname(abspath(__file__))
sys.path.append(root_dir)
