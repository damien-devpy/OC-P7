export class Response {
  /* Create a response object that contain informations from GranPy Bot
  back end. */

  constructor (response) {
    /* Create a response object. */
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
