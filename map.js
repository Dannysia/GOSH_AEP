

function loadMapScenario() {
    
    //map = new Microsoft.Maps.Map(document.getElementById('myMap'), {});
    var map = new Microsoft.Maps.Map('#myMap', {
        credentials: 'ArF9X74BvF7_gQ8upWm40PIJnSZDAvjM26t-E8e0hUQkFjzwjyiI5lMhpf9Ziw_F '
    });

    placePins(map);
}

function placePins(map) {

    //Load the Clustering module.
    Microsoft.Maps.loadModule("Microsoft.Maps.Clustering", function() {

        // Receive pairs of coordinates (lat, long) from the SQL server
        lats = [39.9054895, 0, 0, 0.1];
        longs = [116.3976317, 0, 0.1, 0];
        pins = new Array(lats.length);

        // For each coordinate pair (lat, long): place a pin
        for (let i = 0; i < pins.length; i++) {
            // Create a new pin,
            pins[i] = new Microsoft.Maps.Pushpin(new Microsoft.Maps.Location(lats[i], longs[i]), {
                text: "P"
            });

            // Assign an event handler to the pin
            Microsoft.Maps.Events.addHandler(pins[i], 'click', function() {
                window.location.replace("imagePortal.html?pin=" + i);
            });
        }

        //Create a ClusterLayer and add it to the map.
        var clusterLayer = new Microsoft.Maps.ClusterLayer(pins);
        map.layers.insert(clusterLayer);
    });
}
