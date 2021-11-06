$(document).ready(function(){
    $("a").hover(
        function(){
            $(this).css("background-color", "var(--aep_light_red)");
            $(this).children('a').each(function() {$(this).css("color", "black");});
            //for (var i = 0; i < $(this).children.length; i++) {
               //$(this).children[i].css("visibility", "visible");
                //$(this).children[i].css("color", "black");
            //}
        },
        function(){
            $(this).css("background-color", "var(--aep_dark_red)");
            for (var i = 0; i < $(this).children.length; i++) {
                $(this).children[i].css("visibility", "hidden");
                $(this).children[i].css("color", "white");
            }
        }
    );
});