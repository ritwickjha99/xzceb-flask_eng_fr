'''Translate English to French and Translate french to English'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishText):
    '''Translate English to French'''
    translation = language_translator.translate(
        text = englishText, 
        model_id = 'en-fr').get_result()
    dic = json.loads(json.dumps(translation))
    french_text = dic['translations'][0]['translation']
    return french_text

def french_to_english(frenchText):
    '''Translate french to English'''
    translation = language_translator.translate(
        text=frenchText, 
        model_id='fr-en').get_result()
    dic = json.loads(json.dumps(translation))
    english_text = dic['translations'][0]['translation']
    return english_text
