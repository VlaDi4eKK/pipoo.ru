$(document).ready(function(){
    $(".catalog_nav2").hide();
    $(".catalog_nav li.active ul").show();
    $(".catalog_nav_show").click(function(){
        var ul = $(this).parent("li").children("ul");
        if (ul.css('display') == 'none')
        {
            $(".show").slideUp(300);
            ul.slideDown(300);
            ul.addClass("show");
        }
        else
        {
            ul.slideUp(300);
        }
    });

    $(".left_box_hidden_bottom").click(function(){
        if ($(this).attr("data-show") != 1)
        {
            $(".right_box_forum").hide();
            $(".left_box_hidden").animate({width: '225px'}, 500);
            $(".catalog_nav").css('display', 'block');
            $(".left_box_hidden_bottom").css({'left': '210px', 'border-radius': '8px 0 0 8px'}, 500);
            $(".left_box_hidden_bottom").html('◀');
            $(this).attr("data-show", '1');
        }
        else
        {
            $(".right_box_forum").show();
            $(".left_box_hidden").animate({width: '10px'}, 500);
            $(".left_box_hidden_bottom").animate({'left': '3px'}, 500).delay(500);
            $(".catalog_nav").delay(300).hide(100);
            $(".left_box_hidden_bottom").css('border-radius', '0 8px 8px 0');
            $(".left_box_hidden_bottom").html('▶');
            $(this).attr("data-show", '0');
        }
    });

});