$(document).ready(function(){
    $("a").hover(menuButtonIn(this), menuButtonOut(this));
    function(){
      $(this).css("background-color", "var(--aep_light_red)");
    }, 
    function(){
      $(this).css("background-color", "var(--aep_dark_red)");
    }
    );
  });

function menuButtonIn() {
    $(this).css("background-color", "var(--aep_light_red)");
}

function menuButtonOut() {

}