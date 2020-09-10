export class Response {
  /* Create a response object that contain informations from GranPy Bot
  back end. */

  constructor (response) {
    /* Create a response object.

    Args:

        response (JSON): JSON data containing random message, coordinates,
          extract and url from the back.

    Attributes:

        this._response (string): JSON response parsed
        this._error (string): true or false (Does location has been found
          for instance.)
        this._message (string): random message from GranPy
        this._latitude (string): latitude from location
        this._longitude (string): longitude from location
        this._extract (string): extract from wikipedia
        this._url (string): url for wikipedia page of the location
        this._apiKey (string): Google API Key for Maps API

    */

    this._response = JSON.parse(response)

    this._error = this._response.error
    this._message = this._response.message
    this._latitude = this._response.latitude
    this._longitude = this._response.longitude
    this._extract = this._response.extract
    this._url = this._response.url
    this._apiKey = this._response.apiKey
  }

  getError () {
    return this._error
  }

  getMessage () {
    return this._message
  }

  getResponse () {
    return this._response
  }

  getLatitude () {
    return this._latitude
  }

  getLongitude () {
    return this._longitude
  }

  getExtract () {
    return this._extract
  }

  getUrl () {
    return this._url
  }

  getApiKey () {
    return this._apiKey
  }
}
