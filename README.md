# Harold, GranPy chatbot. Ask him about some places!
### OpenClassrooms - My 7th project for OC PythonPath

#### How is Harold ?

Harold is a world famous hungarian who become a meme at his own expense.

#### How it works:

The point was to built a chatbot that find a place asked by an user, to display it
on a map, and link to his Wikipedia page.

The user input is parsed in order to keep valuable words, the result is passed
to the Google Geocoding API, which return coordinates. 
This coordinates are then used in two ways :

  - Display a map with a cursor on required location (throught JS Google Places API)
  - Forward them to the Wikimedia API to find the most accurate place in all existing
    wikipedia pages.
      
Vanilla JS is implemented in order to manage communication between the front and the back.
(It's so powerful, why using jQuery ?)

Powered by Flask, and of course Python.

### Try it :

Harold is online, and you can try it [here](https://granpy-bot.herokuapp.com/ "Try it !") 

Users inputs and Harold responses are displayed in a conversation window in real time,
just like if you were talking to your Grand Father through Messenger :o)

It's certainly far from being perfect, i'll be glad to have some feedbacks.
Otherwise, if you like it, please consider starring my repo.
        
   
    