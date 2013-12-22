var map;
function initialize(p) {
    var ll = new google.maps.LatLng(p.coords.latitude,p.coords.longitude);
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


var updateCurrent = function() {
    navigator.geolocation.getCurrentPosition(function (p) {
	$.ajax({
	    dataType: 'json',
	    url:'/updateCurrent',
	    data: {'lat':p.coords.latitude,'long':p.coords.longitude},
	    success : function(d) {console.log(d);}
	    })
	});
}


var getCurrents = function() {
    $.getJSON("/getCurrents",function(d) {
	console.log(d);
    });
}



$(document).ready(getLoc);



//google.maps.event.addDomListener(window, 'load', initialize);
