# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-06-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def english_to_french(englishtext):
    if englishtext == '':
        return "No text to translate."

    frenchtext = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    return frenchtext.get('translations')[0].get('translation')

def french_to_english(frenchtext):
    if frenchtext == '':
        return "No text to translate."

    englishtext = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    return englishtext.get('translations')[0].get('translation')

def english_to_spanish(englishtext):
    if englishtext == '':
        return "No text to translate."

    spanishtext = language_translator.translate(
    text=englishtext,
    model_id='en-es').get_result()
    return spanishtext.get('translations')[0].get('translation')

def spanish_to_english(spanishtext):
    if spanishtext == '':
        return "No text to translate."

    englishtext = language_translator.translate(
    text=spanishtext,
    model_id='es-en').get_result()
    return englishtext.get('translations')[0].get('translation')