function foo() {
    //var mapEl = document.getElementById("map");
    //alert(document.getElementsByName("body"));
    if (GBrowserIsCompatible()) {
	var map = new GMap(document.getElementById("map"));
	//map.centerAndZoom(new GPoint(-1.753693, 53.786861), 15);
	//map.centerAndZoom(new GPoint(-1.753693,53.799029), 13);
	map.centerAndZoom(new GPoint(-1.766653,53.791855), 13);
	
	//map.openInfoWindow(map.getCenterLatLng(),
	//	   document.createTextNode("Current location"));

	map.addOverlay(new GMarker(new GPoint(13.23, 52.30)));
	map.addOverlay(new GMarker(new GPoint(2.20, 48.50)));
	map.addControl(new GSmallMapControl());
    }
}

