var map;
function initialize(p) {
    var ll = new google.maps.LatLng(p.coords.latitude,p.coords.longitude);
  var mapOptions = {
    zoom: 12,
    center: ll
  };

  map = new google.maps.Map(document.getElementById('trackmap'),
      mapOptions);
/*
    var marker = new google.maps.Marker({
	position:ll,
	map:map
	//icon:"/static/markers/green_MarkerA.png"
	});
    
*/
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

var markers,marker;
var getCurrents = function() {
    $.getJSON("/getCurrents",function(d) {
	markers=[];
	for (var i = 0 ; i < d.length;i++) {
	    var ll = new google.maps.LatLng(d[i].geo.coordinates[0],
					    d[i].geo.coordinates[1])
	    console.log(ll);
	    var moptions={
		position:ll,
		map:map,
		title:d[i].name};
	    var icon;
	    if (d[i].name==$("#user").val()) 
		icon="/static/markers/green_MarkerA.png";
	    else
		icon="/static/markers/red_MarkerA.png";
	    moptions['icon'] = icon;
	    console.log(moptions);
	    marker = new google.maps.Marker(moptions);
	    markers.push(marker);
	 
	}
	});
}



$(document).ready(getLoc);



//google.maps.event.addDomListener(window, 'load', initialize);
