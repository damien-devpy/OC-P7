export class InputUser {
  /* Create an InputUser object and parse it into JSON.
    */

  constructor (inputUser) {
    /* Turn the input user into a javascript object.

    Args:

        inputUser (object): Raw user input into JS object.

    */

    this._inputUser = {
      sentence: inputUser
    }
  }

  getInputUser () {
    return this._inputUser
  }

  setInputUser (inputUser) {
    this._inputUser.sentence = inputUser
  }

  IntoJSON () {
    /* Parse the input user into a JSON string.

    Parsing occur in place. */

    this._inputUser = JSON.stringify(this._inputUser)
  }
}
