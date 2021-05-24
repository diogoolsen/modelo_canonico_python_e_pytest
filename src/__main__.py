#
# IMPORT
#
# import <PACKAGE>
#
# o import só aceita pacotes e módulos
# - Não podem ser submodulos, subpacotes ou
# outros nomes definidos no pacote\modulo

#
# Importação relativa.
# Considere que a raiz do sistema é a pasta externa a src
#
# Importa os pacotes A e B
# O pacote B está dentro de A e é referenciado no __init__ do pacote A e B
from . import packagea
# Importa o pacote C
from . import packagec


def start():

    print('->', packagea.module_a1.var)
    print('->', packagea.module_a2.var)

    print('->', packagea.packageb.module_b1.var)
    print('->', packagea.packageb.module_b2.var)

    print('->', packagec.module_c1.var)
    print('->', packagec.module_c2.var)


var = '__main__'
