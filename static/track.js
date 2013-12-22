var map;
function initialize(p) {
    console.log(p);
    var ll = new google.maps.LatLng(p.coords.latitude,p.coords.longitude);
    console.log(ll);
  var mapOptions = {
    zoom: 12,
    center: ll
  };

  map = new google.maps.Map(document.getElementById('trackmap'),
      mapOptions);

    var marker = new google.maps.Marker({
	position:ll,
	map:map 
	});
    
}


function getLoc() {
 navigator.geolocation.getCurrentPosition(initialize);
}

$(document).ready(getLoc);



//google.maps.event.addDomListener(window, 'load', initialize);
