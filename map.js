

function loadMapScenario() {
    
    //map = new Microsoft.Maps.Map(document.getElementById('myMap'), {});
    var map = new Microsoft.Maps.Map('#myMap', {
        credentials: 'ArF9X74BvF7_gQ8upWm40PIJnSZDAvjM26t-E8e0hUQkFjzwjyiI5lMhpf9Ziw_F '
    });

    var pushpin = new Microsoft.Maps.Pushpin(map.getCenter(), null);
    map.entities.push(pushpin);

    testMap(map);
}

function testMap(map) {
    //Load the Clustering module.
    Microsoft.Maps.loadModule("Microsoft.Maps.Clustering", function() {

        //Generate 1,000 random pushpins in the map view.
        var pins = Microsoft.Maps.TestDataGenerator.getPushpins(1000, map.getBounds());

        //Create a ClusterLayer and add it to the map.
        var clusterLayer = new Microsoft.Maps.ClusterLayer(pins);
        map.layers.insert(clusterLayer);
    });
}

