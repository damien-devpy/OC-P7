import { InputUser } from './modules/InputUser.js'
import { Response } from './modules/Response.js'

const submitForm = document.body.querySelector('.granpyForm')

submitForm.setAttribute('onsubmit', 'return false')
submitForm.addEventListener('submit', onSubmit)

function onSubmit () {
  const inputUser = new InputUser(submitForm.children[2].value)
  inputUser.IntoJSON()

  const xhr = new XMLHttpRequest()
  xhr.open('POST', '/')
  xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.send(inputUser.getInputUser())

  xhr.onload = function () {
    const response = new Response(xhr.response)

    const newParagraph = document.createElement('p')
    newParagraph.textContent = [response.getLatitude(), response.getLongitude(), response.getExtract(), response.getUrl()]

    document.body.append(newParagraph)
  }

  xhr.onerror = function () {
    document.body.append('Ooops ! Il y a quelque chose qui ne va pas !')
  }
}
