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

    this.showMap()
  }

  mapExist () {
    const gMap = document.getElementById('gMap')

    return gMap
  }

  showMap () {
    const gMap = document.getElementById('gMap')

    gMap.style.display = 'block'
  }

  hideMap () {
    const gMap = document.getElementById('gMap')

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
