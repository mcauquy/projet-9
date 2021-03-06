import logging
import azure.functions as func
import pandas as pd
import numpy as np
import os
import json
from scipy.spatial import distance
from load_data import *
from cont_based import *

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Nouvelle requête HTTP en cours...')

    userid = req.params.get('userid')
    if not userid:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            userid = req_body.get('userId')

    if userid:
        # Chargement des données
        logging.info('Chargement des données en cours ...')
        path = os.getcwd() + '\\globocom\\'
        article_emb, articles, frame = chargement(path)
        logging.info('Le chargement des données est ok')
        
        # Récupération du top5
        logging.info('Récupération des 5 articles en cours ....')
        reco5 = getFiveArticles(article_emb, userid, frame)  
    
        #Envoyer à l'app les 5 articles recommandés
        return func.HttpResponse(json.dumps(reco5), status_code=200)
    else:
        return func.HttpResponse(
             "Pass a userId in the query string or in the request body for a personalized response.",
             status_code=200
        )
