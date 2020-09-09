export class Conversation {
  constructor (input) {
    this.input = input
    this.sectionConversation = document.body.children[1].children[0]
  }

  addInputUser () {
    const newInput = document.createElement('div')
    newInput.className = 'user'

    const newImage = document.createElement('div')
    newImage.className = 'you'

    newInput.textContent = this.input

    // Attach user pict to his input
    newInput.appendChild(newImage)
    this.sectionConversation.append(newInput)

    // Scrolling to user's input
    newInput.scrollIntoView(true)
  }

  addResponseHarold () {
    const newResponseExtract = document.createElement('div')
    newResponseExtract.className = 'granpy'

    const newResponseUrl = document.createElement('a')
    newResponseUrl.className = 'granpy'
    newResponseUrl.href = this.input.getUrl()
    newResponseUrl.textContent = 'Clique ici pour en savoir plus !'

    newResponseExtract.textContent = `${this.input.getExtract()}`

    this.sectionConversation.append(newResponseExtract, newResponseUrl)

    // Scrolling to Harold's response
    newResponseExtract.scrollIntoView(true)
  }

  addMessageHarold () {
    const newMessage = document.createElement('div')
    newMessage.className = 'granpy'

    const newImage = document.createElement('div')
    newImage.className = 'harold'

    newMessage.textContent = `${this.input.getMessage()}`

    // Attach Harold pict to his response
    newMessage.appendChild(newImage)

    this.sectionConversation.append(newMessage)

    // Scrolling to Harold's response
    newMessage.scrollIntoView(true)
  }

  resetForm () {
    const formToReset = document.querySelector('.textbox')
    formToReset.value = formToReset.defaultValue
  }
}
