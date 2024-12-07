# INSTALAR AS BIBLIOTECAS ABAIXO
# pip install openpyxl

import os.path

# UTILIZAÇÃO DE PLANILHAS
from openpyxl import Workbook, load_workbook
from openpyxl.utils import FORMULAE

from datetime import date, datetime
from time import gmtime, strftime 

# BIBLIOTECA PARA CONFIGURAÇÃO DE HORA POR REGIAO
import pytz




# OBTER A HORA UTC PADRÃO
UTC = pytz.utc 

# OBTERÁ O FUSO HORÁRIO
# DA LOCALIZAÇÃO ESPECIFICADA
IST = pytz.timezone('Brazil/East') 


# PRINT O DATE E TIME NO
# FORMATO ESPECIFICADO 
datetime_ist = datetime.now(IST) 



path = "cotacao-" + str(date.today()) + "-time-save-" + str(datetime_ist.strftime('%H-%M-%S')) + ".xlsx"


file  = Workbook()

file.save(path)