# Minha API

Faz parte do projeto de **Desenvolvimento do MVP** que tem como contexto colocar em prática o conteúdo apresentado ao longo das aulas com o desenvolvimento de um back-end e de um front-end, explorando algumas dessas key constraints: (I) a separação de responsabilidades entre cliente e servidor; (II) a uniformidade de interfaces; (III) o desenvolvimento de sistemas em camadas; (IV) a ausência de estados; e (V) a execução de código sob demanda.

Projeto Gerenciador de Estudo faz parte da avaliação da Pós Graduação da Disciplina **Desenvolvimento do MVP** da PUC-Rio.

Escolhi implementar um Gerenciador de Estudo que tem como objetivo fazer o controle de determinadas disciplinas que desejo realizar um estudo para vários tipos de propósito:
concurso, vestibular, estudo de línguas, etc.

## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenpython -m venv .v.pypa.io/en/latest/).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5001 --reload
```

Abra o [http://localhost:5001/#/](http://localhost:5001/#/) no navegador para verificar o status da API em execução.
