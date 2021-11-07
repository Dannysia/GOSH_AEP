function loadImage() { 
    var pin = (new URLSearchParams(window.location.search)).get("pin");

    var img = document.createElement("IMG");
    img.id = "droneShot";
    img.src = "http://174.138.39.166:3000/image/" + (pin);

    document.getElementById("imgContainer").appendChild(img);
}


