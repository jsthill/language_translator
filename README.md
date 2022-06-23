# Language Translator
This project was built using Html, JavaScript, and Python3. The purpose of the project is to do the following.
1. Convert English to French
2. Convert English to Spanish
3. Convert French to English
4. Convert Spanish to English

The project uses IBM-Watson language translator services to do the conversion. For this project to work on your server you need to do the following.
1. Create an IBM Cloud account if you don't already have one.
2. Add the language translator services.
3. Copy the key and URL for the service. They will be used by the Python script translator.py.
4. Create a .env file under the <b>machinetranslation</b> folder.
5. Add the following lines of code to the .env file and save it.

  apikey ="<em><The key you copied from step 3.></em>"
  
  url = "<em><The URL you copied from step 3.></em>"
  
To run the project navigate to the "final_project" folder and run the server.py script.
  
Have fun! 😎
