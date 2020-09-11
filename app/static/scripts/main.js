import { InputUser } from './modules/InputUser.js'
import { Response } from './modules/Response.js'
import { GoogleMap } from './modules/GoogleMap.js'
import { Conversation } from './modules/Conversation.js'

const submitForm = document.body.querySelector('.granpyForm')

submitForm.setAttribute('onsubmit', 'return false')
submitForm.addEventListener('submit', onSubmit)

function onSubmit () {
  const input = submitForm.children[2].value

  // If the user input isn't empty
  if ((input.trim())) {
    const conversation = new Conversation(input)

    // Reset the form and display user input to the conversation window
    conversation.resetForm()
    conversation.addInputUser()

    const inputUser = new InputUser(input)
    inputUser.IntoJSON()

    // Create an AJAX request and sending input user (turn to JSON data)
    // to the flask view
    const xhr = new XMLHttpRequest()
    xhr.open('POST', '/')
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(inputUser.getInputUser())

    // When response come back from back-end, displaying GranPy random message
    // response and wikipedia informations to conversation window.
    xhr.onload = function () {
      const response = new Response(xhr.response)
      const googleMap = new GoogleMap(response)

      const conversation = new Conversation(response)
      conversation.addMessageHarold()

      if (response.getError() === 'false') {
        conversation.addResponseHarold()

        // If Map is already displed, updating it.
        if (googleMap.mapExist()) {
          googleMap.updateMap(response)
        // Else, create it, add it to DOM and display it.
        } else if (!googleMap.mapExist()) {
          googleMap.addMap()
        }

        googleMap.showMap()
      }
    }

    xhr.onerror = showError
  }
}

function showError () {
  document.body.children[1].children[0].append('Ooops ! Il y a quelque chose qui ne va pas !')
}
