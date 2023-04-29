import datetime
from pydantic import BaseModel
from typing import Optional, List
from model.estudo import Estudo
from sqlalchemy import DateTime,Column,Date
from datetime import date
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.sql import func





class EstudoSchema(BaseModel):
    """ Define como um nova disciplina estudada a ser inserido deve ser representado
    """
    disciplina: str = "Desenvolvimento Full Stack"
    conteudo: str = "TESTE"
    contato:  str = "sim"
    primeira_revisao: str = "03/03/2023"
    segunda_revisao : str = "11/03/2023"
    questao_feita   :int = 12
    questao_acertada: int = 10
    # data_primeira_revisao:  Optional [Date] = None
     #data_primeira_revisao:  Date = None 
    #data_primeira_revisao:  Date = datetime(2022, 5, 27, 12, 30, 0, 0)

    #DateTime(default=datetime.datetime.now())

    

class EstudoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da dsiciplina.
    """
    id: int = 1


class ListagemEstudosSchema(BaseModel):
    """ Define como uma listagem de estudos será retornada.
    """
    estudos:List[EstudoSchema]


def apresenta_estudos(estudos: List[Estudo]):
    """ Retorna uma representação do produto seguindo o schema definido em
        EstudoViewSchema.
    """
    result = []
    for estudo in estudos:
        result.append({
            "id": estudo.id,
            "disciplina": estudo.disciplina,
            "conteudo": estudo.conteudo,
            "contato": estudo.contato,
            "primeira_revisao": estudo.primeira_revisao,
            "segunda_revisao": estudo.segunda_revisao,
            "questao_feita": estudo.questao_feita,
            "questao_acertada": estudo.questao_acertada,
        })

    return {"estudos": result}


class EstudoViewSchema(BaseModel):
    """ Define como um estudo que será retornado: disciplina + questões.
    """
    id: int = 1
    disciplina: str = "ARQUITETURA"
    conteudo: str = "DDD, arquitetura hexagonal, microsserviços (orquestração de serviços e API gateway) e containers."
    contato: str = "teste"
    primeiraRevisao: str = "01/02/2023"
    segundaRevisao: str = "01/03/2023"
    questao_feita: int = 30
    questao_acertada: int = 20
    #data_primeira_revisao: Date = datetime(2022, 5, 27, 12, 30, 0, 0)
    # data_primeira_revisao: Date = None



class EstudoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    disciplina: str

def apresenta_estudo(estudo: Estudo):
    """ Retorna uma representação do estudo seguindo o schema definido em
        EstudoViewSchema.
    """
    return {
        "id": estudo.id,
        "disciplina": estudo.disciplina,
        "conteudo":   estudo.conteudo,
        "contato":   estudo.contato,
        "primeira_revisao": estudo.primeira_revisao,
        "segunda_revisao": estudo.segunda_revisao,
        "questao_feita": estudo.questao_feita,
        "questao_acertada": estudo.questao_acertada,
        #"data_primeira_revisao": estudo.data_primeira_revisao        
       
    }
