$(document).ready(() => {
    console.log("Hello ji")
    $(window).on('scroll',function() {
        let ratio = ($(window).scrollTop())/($(document).height() - $(window).height())
        $('#under').css('top', String(ratio*($(window).height()) + 100) + 'px')
        console.log()
    })
})
