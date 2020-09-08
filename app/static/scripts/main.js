import { InputUser } from './modules/InputUser.js'
import { Response } from './modules/Response.js'
import { GoogleMap } from './modules/GoogleMap.js'

const submitForm = document.body.querySelector('.granpyForm')

submitForm.setAttribute('onsubmit', 'return false')
submitForm.addEventListener('submit', onSubmit)

const sectionConversation = document.body.children[1].children[0]

function onSubmit () {
  hideDivMap()

  const input = submitForm.children[2].value

  addInputUsertoDOM(input)

  const inputUser = new InputUser(input)
  inputUser.IntoJSON()

  const xhr = new XMLHttpRequest()
  xhr.open('POST', '/')
  xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.send(inputUser.getInputUser())

  xhr.onload = function () {
    const response = new Response(xhr.response)
    const googleMap = new GoogleMap(response)

    addResponseHaroldtoDOM(response)

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

function addInputUsertoDOM (input) {
  const newInput = document.createElement('div')
  newInput.className = 'user'
  const newImage = document.createElement('div')
  newImage.className = 'you'

  newInput.textContent = input

  newInput.appendChild(newImage)

  sectionConversation.append(newInput)

  newInput.scrollIntoView(true)
}

function addResponseHaroldtoDOM (response) {
  const newResponseExtract = document.createElement('div')
  newResponseExtract.className = 'granpy'

  const newResponseUrl = document.createElement('a')
  newResponseUrl.className = 'granpy'
  newResponseUrl.href = response.getUrl()
  newResponseUrl.textContent = 'Clique ici pour en savoir plus !'

  const newImage = document.createElement('div')
  newImage.className = 'harold'

  newResponseExtract.textContent = `${response.getExtract()}`

  newResponseExtract.appendChild(newImage)

  sectionConversation.append(newResponseExtract, newResponseUrl)

  newResponseExtract.scrollIntoView(true)
}
