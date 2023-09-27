from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session
from logger import logger
from model.estudo import Estudo
from schemas import *
from flask_cors import CORS
#import debugpy

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)


CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
estudo_tag = Tag(name="Estudo", description="Adição, visualização e remoção de estudos à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/estudo', tags=[estudo_tag],
          responses={"200": EstudoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_estudo(form: EstudoSchema):
    """Adiciona um novo Estudo à base de dados

    Retorna uma representação dos estudos.
    """
    estudo = Estudo(
        disciplina=form.disciplina,
        conteudo=form.conteudo,
        contato=form.contato,
        primeira_revisao=form.primeira_revisao,
        segunda_revisao=form.segunda_revisao,
        questao_feita=form.questao_feita,
        questao_acertada=form.questao_acertada,
        banca = form.banca,
        endereco = form.endereco,
       # data_primeira_revisao = form.data_primeira_revisao
        )
    logger.debug(f"Adicionando estudo cuja disciplina é de nome: '{estudo.disciplina}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando estudo
        session.add(estudo)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado estudo cuja disciplina é de nome: '{estudo.disciplina}'")
        return apresenta_estudo(estudo), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Estudo de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar estudo '{estudo.disciplina}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar estudo '{estudo.disciplina}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/estudos', tags=[estudo_tag],
         responses={"200": ListagemEstudosSchema, "404": ErrorSchema})
def get_estudos():
    """Faz a busca por todos os Estudos cadastrados

    Retorna uma representação da listagem de estudos.
    """
    logger.debug(f"Coletando estudos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    estudos = session.query(Estudo).all()

    if not estudos:
        # se não há estudos cadastrados
        return {"estudos": []}, 200
    else:
        logger.debug(f"%d estudos econtrados" % len(estudos))
        # retorna a representação de estudo
        print(estudos)
        return apresenta_estudos(estudos), 200


@app.get('/estudo', tags=[estudo_tag],
         responses={"200": EstudoViewSchema, "404": ErrorSchema})
def get_estudo(query: EstudoBuscaSchema):
    """Faz a busca por um Estudo a partir do id do estudo

    Retorna uma representação dos estudos.
    """
    estudo_id = query.id
    logger.debug(f"Coletando dados sobre estudo #{estudo_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    estudo = session.query(Estudo).filter(Estudo.id == estudo_id).first()

    if not estudo:
        # se o estudo não foi encontrado
        error_msg = "Estudo não encontrado na base :/"
        logger.warning(f"Erro ao buscar estudo '{estudo_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Estudo  econtrado: '{estudo.disciplina}'")
        # retorna a representação do estudo
        return apresenta_estudo(estudo), 200


@app.delete('/estudo', tags=[estudo_tag],
            responses={"200": EstudoDelSchema, "404": ErrorSchema})
def del_estudo(query: EstudoBuscaSchema):
    """Deleta um Estudo a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
   #estudo_disciplina = unquote(unquote(query.disciplina))
    estudo_disciplina =query.id

    print(estudo_disciplina)
    logger.debug(f"Deletando dados sobre estudo #{estudo_disciplina}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Estudo).filter(Estudo.id == estudo_disciplina).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado estudo #{estudo_disciplina}")
        return {"mesage": "Estudo removido", "id": estudo_disciplina}
    else:
        # se o estudo não foi encontrado
        error_msg = "Estudo não encontrado na base :/"
        logger.warning(f"Erro ao deletar estudo #'{estudo_disciplina}', {error_msg}")
        return {"mesage": error_msg}, 404



@app.put('/estudo', tags=[estudo_tag],
          responses={"200": EstudoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def atualiza_estudo(form: EstudoSchema):
    """Edita um novo Estudo/disciplina já salvo na base de dados

    Retorna uma representação dos estudos/disciplinas.
    """
    
    nome_estudo = form.disciplina # nome do estudo/disciplina que será atualizado
    
    logger.debug(f"Atualizando estudo/disicplina de nome: '{form.disciplina}'")
    try:
        # criando conexão com a base
        session = Session()
        # buscando o produto na base de dados
        updated_estudo = session.query(Estudo).filter(Estudo.disciplina == nome_estudo).first()

        # se o produto não estiver cadastrado na base de dados
        if not updated_estudo:
            error_msg = "Estudo/Disciplina não cadastrada no banco de dados :/"
            return {"mesage": error_msg}, 404
        else:
            # se foi informado um novo valor referente a quantidade
            if form.contato:
                updated_estudo.contato = form.contato
            
            # se foi informado um novo valor referente ao valor
            if form.questao_feita:
                updated_estudo.questao_feita = form.questao_feita 
                
             # se foi informado um novo valor referente ao valor
            if form.questao_acertada:
                updated_estudo.questao_acertada = form.questao_acertada 
                
            session.add(updated_estudo) #atualizando o estudo/disciplina na base de dados

            # efetivando o camando de atualização do item na tabela
            session.commit()
            logger.debug(f"Atualizando estudo de nome de disciplina: '{form.disciplina}'")
            return apresenta_estudo(updated_estudo), 200

    except IntegrityError as e:
        # como a duplicidade do nome disciplina é a provável razão do IntegrityError
        error_msg = "Estudo/Discplina de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar estudo/disciplina '{form.disciplina}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar disciplina '{form.disciplina}', {error_msg}")
        return {"mesage": error_msg}, 400