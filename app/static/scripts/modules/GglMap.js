export class GglMap {
  /* Create a Map object. Contain coordinates and display a Google Map
    throught the Javascript API. */

  constructor (responseObject) {
    this.latitude = responseObject.getLatitude()
    this.longitude = responseObject.getLongitude()
    this.url = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyCRPxd_MbmjNUTwa1xtVWuKjfIllD3lOXY'
    this.callback = '&callback=loadMap'
  }

  addScriptCallAPI () {
    const newScript = document.createElement('script')

    newScript.src = this.url + this.callback

    document.head.append(newScript)
  }

  addScriptMap () {
    const newDiv = document.createElement('div')
    newDiv.id = 'map'

    document.body.append(newDiv)

    const newScript = document.createElement('script')

    newScript.text = `
        function loadMap() {
            let map;
            let marker;
            let coordinates = {lat: ${this.latitude}, lng: ${this.longitude}};

            map = new google.maps.Map(document.getElementById('map'), {
                center: coordinates,
                zoom: 8
            });

            marker = new google.maps.Marker({
                position: coordinates,
                map: map
            });
        };`

    document.head.append(newScript)
  }

/*  deleteMap () {
    const divMap = document.getElementById('map')

    divMap.remove()
  } */
}
