#!/usr/bin/env python3

import logging
import os
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

#Nossa instancia
log = logging.Logger("Alex", log_level)
#Level
#ch = logging.StreamHandler() #Console/terminal/stderr
fh = handlers.RotatingFileHandler("meu_log.log", maxBytes=10**6, backupCount=10)
#ch.setLevel(log_level)
#Formatação
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
#Destino
log.addHandler(fh)

"""
log.debug("Mensagem pro dev, QA, sysadmin")
log.info("Mensagem geral para usúarios")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta um unico user")
log.critical("Erro geral Ex: O db pirou e dropou tudo")
"""
print("-" *  3)

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro no %s",str(e))
    