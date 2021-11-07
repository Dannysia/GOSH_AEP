function loadMapScenario() {
    
    //map = new Microsoft.Maps.Map(document.getElementById('myMap'), {});
    var map = new Microsoft.Maps.Map('#myMap', {
        credentials: 'ArF9X74BvF7_gQ8upWm40PIJnSZDAvjM26t-E8e0hUQkFjzwjyiI5lMhpf9Ziw_F '
    });

    placePins(map);
}


var imageIDs;


function placePins(map) {

    //Load the Clustering module.
    Microsoft.Maps.loadModule("Microsoft.Maps.Clustering", function() {

        var lats;
        var longs;
        // Receive pairs of coordinates (lat, long) from the SQL server
        $.getJSON('http://174.138.39.166:3000/getLocations', function(data) {
            var size = data.length;
            lats = new Array(size);
            longs = new Array(size);
            imageIDs = new Array(size);
            

            for (var i = 0; i < data.length; i++) {
                imageIDs[i] = data[i]["ImageID"];
                lats[i] = data[i]["Latitude"];
                longs[i] = data[i]["Longitude"];
            }

            var pins = new Array(lats.length);

            // For each coordinate pair (lat, long): place a pin
            for (let i = 0; i < pins.length; i++) {
                // Create a new pin,
                pins[i] = new Microsoft.Maps.Pushpin(new Microsoft.Maps.Location(lats[i], longs[i]));

                // Assign an event handler to the pin
                Microsoft.Maps.Events.addHandler(pins[i], 'click', function() {
                    window.location.replace("report.html?pin=" + imageIDs[i]);
                });
            }

            //Create a ClusterLayer and add it to the map.
            var clusterLayer = new Microsoft.Maps.ClusterLayer(pins);
            map.layers.insert(clusterLayer);
        });
    });
}
