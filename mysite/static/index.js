$(document).ready(() => {
    console.log("Hello ji")
    $(window).on('scroll',function() {
        let ratio = ($(window).scrollTop())/($(document).height() - $(window).height())
        $('#under').css('top', String(ratio*($(window).height()) + 100) + 'px')
        console.log()
    })
})

$(document).ready(function(){
  $("a").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
        window.location.hash = hash;
      });
    } 
  });
});