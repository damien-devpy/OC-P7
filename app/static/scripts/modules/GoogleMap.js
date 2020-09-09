export class GoogleMap {
  /* Create a Map object. Contain coordinates and display a Google Map
    throught the Javascript API. */

  constructor (responseObject) {
    this.latitude = responseObject.getLatitude()
    this.longitude = responseObject.getLongitude()
    this.coordinates = { lat: this.latitude, lng: this.longitude }
    this.apiKey = responseObject.getApiKey()
    this.url = `https://maps.googleapis.com/maps/api/js?key=${this.apiKey}`
    this.callback = '&callback=loadMap'

    this.sectionGoogleMap = document.body.children[1].children[1]
  }

  addMap () {
    this._addScriptCallAPI()
    this._addScriptMap()
  }

  updateMap (responseObject) {
    this.latitude = responseObject.getLatitude()
    this.longitude = responseObject.getLongitude()

    const newScript = document.createElement('script')

    newScript.text = `
        coordinates = {lat: ${this.latitude}, lng: ${this.longitude}};

        loadMap()

    `

    document.head.append(newScript)
  }

  mapExist () {
    const gMap = document.getElementById('gMap')

    return gMap
  }

  showMap () {
    const centralZone = document.querySelector('.central-zone')
    const conversation = document.querySelector('.conversation')
    const gMap = document.querySelector('.gMap')

    centralZone.style.gridTemplateColumns = '50% 50%'

    conversation.style.gridColumn = '1 / 2'

    gMap.style.display = 'block'
  }

  hideMap () {
    const centralZone = document.querySelector('.central-zone')
    const conversation = document.querySelector('.conversation')
    const gMap = document.querySelector('.gMap')

    centralZone.style.gridTemplateColumns = '25% 25% 25% 25%'
    conversation.style.gridColumn = '2 / 4'
    gMap.style.display = 'none'
  }

  _addScriptCallAPI () {
    const newScript = document.createElement('script')
    newScript.src = this.url + this.callback

    document.head.append(newScript)
  }

  _addScriptMap () {
    const newDiv = document.createElement('div')
    newDiv.id = 'gMap'

    this.sectionGoogleMap.append(newDiv)

    const newScript = document.createElement('script')
    newScript.text = `
        let googleMap;
        let marker;
        let coordinates = {lat: ${this.latitude}, lng: ${this.longitude}};

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
