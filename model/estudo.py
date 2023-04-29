from datetime import datetime
from typing import Union
from sqlalchemy import Column, DateTime, Date,Float, Integer, String,Date

from  model import Base
import datetime
#from datetime import date
#from datetime import datetime
from sqlalchemy.sql import func



class Estudo(Base):
    __tablename__ = 'estudo'

    id = Column("pk_estudo", Integer, primary_key=True)
    disciplina = Column(String(140), unique=True)
    conteudo = Column(String)
    contato = Column(String)
    primeira_revisao = Column(String)
    segunda_revisao = Column(String)
    questao_feita = Column(Integer)
    questao_acertada = Column(Integer)

    data_insercao = Column(DateTime)

    #data_primeira_revisao = Column(Date)
    #data_primeira_revisao = Column(DateTime(timezone=True), server_default=func.now())


    def __init__(self, disciplina:str,conteudo:str,contato:str,primeira_revisao:str,segunda_revisao:str,questao_feita:int, questao_acertada:int,
                  data_insercao:Union[DateTime, None] = None,data_primeira_revisao:Union[DateTime, None] = None):
                 # data_primeira_revisao:Union[Date, None] = None):
        """
        Cria um Estudo de um Disciplina

        Arguments:
            disciplina: nome da disciplina.
            contato: primeiro contato ou não da dsiciplina
            conteudo: conteudo da disciplona
            primeira_revisao: revisou a primeira vez
            segunda_revisao: revisou a segunda vez
            questao_feita: qtde de questões feitas
            questao_acertada: qtde de questões acertadas
            data_insercao: data de quando a disciplina foi inserido à base
            data_primeira_revisao: data de quando revisou a primeira vez

        """
        
        self.disciplina = disciplina
        self.conteudo = conteudo
        self.contato =  contato
        self.primeira_revisao = primeira_revisao 
        self.segunda_revisao = segunda_revisao
        self.questao_feita = questao_feita
        self.questao_acertada = questao_acertada
        self.data_primeira_revisao = data_primeira_revisao
       

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

 

