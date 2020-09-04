export class Response {
  /* Create a response object that contain informations from GranPy Bot
  back end. */

  constructor (response) {
    /* Create a response object. */
    this._response = response;

    [this._latitude,
      this._longitude,
      this._extract,
      this._url] = this._parseResponse()
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

  _parseResponse () {
    this._response = JSON.parse(this._response)

    return [this._response.latitude,
      this._response.longitude,
      this._response.extract,
      this._response.url]
  }
}
