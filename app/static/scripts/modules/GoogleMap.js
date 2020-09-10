export class GoogleMap {
  /* Create a Google Map object. Contain coordinates and display a Google Map
    throught the Javascript API. */

  constructor (responseObject) {
    /* Create a Google Map object.

    Args:

        responseObject (object): Contain granpy response from an input user

    Attributes:

      this._latitude (string): latitude from location
      this._longitude (string): latitude from location
      this._coordinates (object): coordinates from location
      this._apiKey (string): Google API key for Maps API
      this._url (string): url for wikipedia page
      this._callback (string): JS function to call when Maps API got loaded
      this._sectionGoogleMap (object): Object from DOM API
      this._mediaQuery (MediaQueryList): Informations for detecting mobile phone

    */

    this._latitude = responseObject.getLatitude()
    this._longitude = responseObject.getLongitude()
    this._coordinates = { lat: this._latitude, lng: this._longitude }
    this._apiKey = responseObject.getApiKey()
    this._url = `https://maps.googleapis.com/maps/api/js?key=${this._apiKey}`
    this._callback = '&callback=loadMap'

    this._sectionGoogleMap = document.body.children[1].children[1]
    this._mediaQuery = window.matchMedia('(max-width: 1024px)').matches
  }

  addMap () {
    /* Add Google Map to the DOM. */

    this._addScriptCallAPI()
    this._addScriptMap()
  }

  updateMap (responseObject) {
    /* Updating Google Map with new location. */

    this._latitude = responseObject.getLatitude()
    this._longitude = responseObject.getLongitude()

    const newScript = document.createElement('script')

    newScript.text = `
        coordinates = {lat: ${this._latitude}, lng: ${this._longitude}};

        loadMap()

    `

    document.head.append(newScript)
  }

  mapExist () {
    /* Check if Google Map already exist in the DOM.

    Return:

      bool: true if the Map already exist, false otherwise

    */

    const gMap = document.getElementById('gMap')

    return Boolean(gMap)
  }

  showMap () {
    /* Display the map. */

    // If user using mobile phone or any tiny screen
    if (this._mediaQuery) {
      const conversation = document.querySelector('.conversation')
      const gMap = document.querySelector('.gMap')

      conversation.style.gridRow = '1 / 2'

      gMap.style.display = 'block'
    } else {
      const centralZone = document.querySelector('.central-zone')
      const conversation = document.querySelector('.conversation')
      const gMap = document.querySelector('.gMap')

      centralZone.style.gridTemplateColumns = '50% 50%'

      conversation.style.gridColumn = '1 / 2'

      gMap.style.display = 'block'
    }
  }

  hideMap () {
    /* Hide the map. */

    // If user using mobile phone or any tiny screen
    if (this._mediaQuery) {
      const conversation = document.querySelector('.conversation')
      const gMap = document.querySelector('.gMap')

      conversation.style.gridRow = '1 / 3'

      gMap.style.display = 'none'
    } else {
      const centralZone = document.querySelector('.central-zone')
      const conversation = document.querySelector('.conversation')
      const gMap = document.querySelector('.gMap')

      centralZone.style.gridTemplateColumns = '25% 25% 25% 25%'
      conversation.style.gridColumn = '2 / 4'
      gMap.style.display = 'none'
    }
  }

  _addScriptCallAPI () {
    /* Add script to the DOM that will call for Google API. */

    const newScript = document.createElement('script')
    newScript.src = this._url + this._callback

    document.head.append(newScript)
  }

  _addScriptMap () {
    /* Add scripts to the DOM that will allow to display the map. */

    const newDiv = document.createElement('div')
    newDiv.id = 'gMap'

    this._sectionGoogleMap.append(newDiv)

    const newScript = document.createElement('script')
    newScript.text = `
        let googleMap;
        let marker;
        let coordinates = {lat: ${this._latitude}, lng: ${this._longitude}};

        function loadMap() {

            googleMap = new google.maps.Map(document.getElementById('gMap'), {
                center: coordinates,
                zoom: 8,
            });

            marker = new google.maps.Marker({
                position: coordinates,
                map: googleMap,
            });
        };
    `

    document.head.append(newScript)
  }
}
