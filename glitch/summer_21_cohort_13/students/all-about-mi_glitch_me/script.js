$(function() {
  var text = $(".text");
  $(window).scroll(function() {
    var scroll = $(window).scrollTop();

    if (scroll >= 200) {
      text.removeClass("hidden");
    } else {
      text.addClass("hidden");
    }
  });
});

