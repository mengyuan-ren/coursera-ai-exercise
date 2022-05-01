'''
Provides translation between english and french
'''

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

def english_to_french(english_text):
    '''
    Takes an english text input to translate to french text as output
    '''
    if english_text is None:
        return ''
    
    french_translation=language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    translation = french_translation['translations'][0]['translation']
    return translation

def french_to_english(french_text):
    '''
    Takes an fnglish text input to translate to erench text as output
    '''
    if french_text is None:
        return ''
    
    english_translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    translation = english_translation['translations'][0]['translation']
    return translation
