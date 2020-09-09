import { InputUser } from './modules/InputUser.js'
import { Response } from './modules/Response.js'
import { GoogleMap } from './modules/GoogleMap.js'
import { Conversation } from './modules/Conversation.js'

const submitForm = document.body.querySelector('.granpyForm')

submitForm.setAttribute('onsubmit', 'return false')
submitForm.addEventListener('submit', onSubmit)

function onSubmit () {
  const input = submitForm.children[2].value

  if ((input.trim())) {
    let conversation = new Conversation(input)

    // Reset the form and add user's input to the conversation window
    conversation.resetForm()
    conversation.addInputUser()

    const inputUser = new InputUser(input)
    inputUser.IntoJSON()

    const xhr = new XMLHttpRequest()
    xhr.open('POST', '/')
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(inputUser.getInputUser())

    xhr.onload = function () {
      const response = new Response(xhr.response)
      const googleMap = new GoogleMap(response)

      conversation = new Conversation(response)
      conversation.addMessageHarold()

      if (response.getError() === 'false') {
        conversation.addResponseHarold()

        if (googleMap.mapExist()) {
          googleMap.updateMap(response)
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
