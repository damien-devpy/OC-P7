const submitForm = document.body.querySelector('.granpyForm')

submitForm.setAttribute('onsubmit', 'return false')
submitForm.addEventListener('submit', onSubmit)

function onSubmit () {
  alert('Dans onSubmit')

  const newParagraph = document.createElement('p')

  newParagraph.textContent = submitForm.children[2].value

  alert(newParagraph.textContent)

  data = {
    input: newParagraph.textContent
  }

  dataJSON = JSON.stringify(data)

  alert(typeof dataJSON)

  document.body.append(dataJSON)

  const xhr = new XMLHttpRequest()

  xhr.open('POST', '/')

  xhr.setRequestHeader('Content-Type', 'application/json')

  xhr.send(dataJSON)

  xhr.onload = function () {
    alert(xhr.response)
  }
}
