
var track = function() {
    
    var map,markers,marker;

    function initializeMap(p) {
	var ll = new google.maps.LatLng(p.coords.latitude,p.coords.longitude);
	var mapOptions = {
	    zoom: 12,
	    center: ll
	};
	
	map = new google.maps.Map(document.getElementById('trackmap'),
				  mapOptions);

	getCurrents();
	updateCurrent();

    }

    /*
     Make the initial google map by getting the current location and 
     draw the initial map (no markers yet)
     */
    function getInitialLoc() {
	navigator.geolocation.getCurrentPosition(initializeMap);
    }
    
    /*
     Update the current users location by making a call to the server
     with the current location
     */
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
    
    /*
     Get all the people logged in from the server and draw markers for each.
     by resetting markers to the empty array[] we get rid of the old marers each time
     */
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

    var timer;

    var updateAll = function() {
	getCurrents();
	updateCurrent();
    }

    var setupTimers = function() {
	timer = setInterval(updateAll,1000*60);
    }
	
    return {
	getCurrents: getCurrents,
	updateCurrent: updateCurrent,
	initialize: getInitialLoc,
	setupTimers: setupTimers
	};
    }()

$(document).ready(function() {
    track.initialize();
    track.setupTimers();
});









