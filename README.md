# Modelo Canônico de Projetos em Python com pytest

Este repositório apresenta um modelo de projetos baseado nas boas práticas de programação em python (PEP8) e pytest (configuração e estrutura de diretórios).

## Estrutura de Diretórios 

Fontes:

- https://docs.pytest.org/en/reorganize-docs/new-docs/user/directory_structure.html
- https://www.python.org/dev/peps/pep-0008/#naming-conventionshttps://www.python.org/dev/peps/pep-0008/#naming-conventions

​    A estrutura básica de diretórios sugerida pelo pytest se baseia em separar o código fonte (diretório src) da estrutura de testes (diretório tests). Uma boa prática de programação em python é seguir o a convenção de nomes proposta pelo PEP8, que define que nomes de pacotes e módulos devem ser em caixa baixa e, se necessário para melhorar a legibilidade, separados pelo carácter de sublinhado (*underscore*), sendo que o uso de sublinhado em pacotes é desencorajado. O pytest, por sua vez, recomenda que que diretórios e arquivos que contém testes iniciem com os prefixos "tests\_" e "test\_", respectivamente. Os diretórios dos testes também devem espelhar a estrutura de diretórios do código. 

​    Assim, este modelo canônico propõe a seguinte estrutura de diretórios para os projetos:

```pseudocode
root
+-- app.py				# Lançador do app
+-- conftest.py			# Arquivo que configura os testes
+-- src						# Código fonte da aplicação
|	+-- __init__.py				# Transforma o src em um pacote importável
|	+-- __main__.py				# Configura a inicialização da aplicação
|	+-- packagea				# Pacote A
|	|	+-- __init__.py			# Transforma o package_A em um pacote importável
|	|	+-- module_a1.py		# Primeiro módulo do pacote A
|	|	+-- module_a2.py		# Segundo módulo do pacote A
|	|	+-- packageb			# Pacote A.B
|	|	|	+-- __init__.py
|	|	|	+-- module_b1.py
|	|	|	+-- module_b2.py
|	+-- packagec				# Pacote C
|	|	+-- __init__.py
|	|	+-- module_c1.py
|	|	+-- module_c2.py
+-- tests					# Códigos de teste da aplicação
|	+-- tests_packagea			# Diretório contendo os testes do pacote A
|	|	+-- test_module_a1.py	# Testes do primeiro módulo do pacote A
|	|	+-- test_module_a2.py	# Testes do segundo módulo do pacote A
|	|	+-- tests_packageb		# Diretório contendo os testes do pacote A.B 
|	|	|	+-- test_module_b1.py
|	|	|	+-- test_module_b2.py
|	+-- tests_packagec			# Diretório contendo os testes do pacote C
|	|	+-- test_module_c1.py
|	|	+-- test_module_c2.py
```

## Configuração dos diretórios do pytest

​    O pytest busca e executa cada módulo de testes de forma independente do projeto e sem respeitar a raiz do projeto (diretório root) o que pode atrapalhar no processo de importação dos módulos do projeto pelo pytest. Para corrigir este processo, pode-se usar o comando `python -m pytest` na pasta raiz do sistema ou, preferencialmente configurar o arquivo `conftest.py` adicionando a raiz do sistema na variável `__path__` do python, fazendo com que o python procure os pacotes e módulos a serem importados também a partir da da raiz do sistema. 

​    Para isso o arquivo `conftest.py` possui o seguinte conteúdo:

```python
import sys
from os.path import dirname, abspath

root_dir = dirname(abspath(__file__))
sys.path.append(root_dir)
```

## Importação de pacotes e módulos

​    A importação de pacotes e módulos em python pode apresentar certa complexidade. Existem duas formas de se importar nomes para o escopo de um código, sendo:

- Importação com endereço **absoluto**: quando se apresenta o caminho completo da raiz do sistema até o que se deseja importar (que pode ser um pacote, módulo, classe, variável, ...).
- Importação com endereço **relativo**: neste caso o endereço apresentado usa como referência o arquivo atual e não a raiz do sistema.

​    Além disso, pode-se usar duas sintaxes para a importação, sendo:

- `import <NOME>`: Importa pacotes e/ou módulos para o espaço de nomes do python.
- `from <CAMINHO> import <NOME>`: Permite a importação, a partir de um caminho, de pacotes e/ou módulo para o escopo da aplicação, porém, também permite a importação de sub-módulos - ou partes de um módulo ou pacote - como classes, métodos, funções, variáveis, ...

​    Uma boa prática de programação é importar apenas o que se pretende usar, evitando a importação de nomes desnecessários, que podem demorar para carregar, gastar recursos computacionais em excesso e poluir o espaço de nomes da aplicação - podendo causar inconsistências no mesmo. Outra boa prática é o uso de importações usando caminhos relativos, pois são mais flexíveis e facilitam o reuso de pacotes e módulos dentro de outras aplicações.

​    O processo de importação no python envolve ainda outros componentes, portanto deixo aqui o link para a documentação deste processo: https://docs.python.org/3/reference/import.html.

​    Obs: o uso de `from <CAMINHO> import *` é desaconselhável.

## Executando o modelo e seus testes

​    O python e o pytest devem estar instalados e operando. Para executar o modelo, entre na raiz do sistema e use o comando `$ python app.py`; para executar os testes, na raiz do sistema use o comando `pytest`. 