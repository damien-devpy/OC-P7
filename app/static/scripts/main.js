import { InputUser } from './modules/InputUser.js'
import { Response } from './modules/Response.js'
import { GoogleMap } from './modules/GoogleMap.js'

const submitForm = document.body.querySelector('.granpyForm')

submitForm.setAttribute('onsubmit', 'return false')
submitForm.addEventListener('submit', onSubmit)

const sectionConversation = document.body.children[1].children[0]
const sectionGoogleMap = document.body.children[1].children[1]
const sectionForm = document.body.children[3]

function onSubmit () {
  hideDivMap()

  const inputUser = new InputUser(submitForm.children[2].value)
  inputUser.IntoJSON()

  const xhr = new XMLHttpRequest()
  xhr.open('POST', '/')
  xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.send(inputUser.getInputUser())

  xhr.onload = function () {
    const response = new Response(xhr.response)
    const googleMap = new GoogleMap(response)

    const newParagraph = document.createElement('p')
    newParagraph.textContent = [response.getLatitude(), response.getLongitude(), response.getExtract(), response.getUrl()]

    sectionConversation.append(newParagraph)

    if (googleMap.mapExist()) {
      googleMap.updateMap(response)
    } else {
      googleMap.addMap()
    }
  }

  xhr.onerror = showError
}

function hideDivMap () {
  const gMap = document.getElementById('gMap')
  if (gMap) {
    gMap.style.display = 'none'
  }
}

function showError () {
  sectionConversation.append('Ooops ! Il y a quelque chose qui ne va pas !')
}
