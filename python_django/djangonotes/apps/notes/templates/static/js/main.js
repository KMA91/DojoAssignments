$( document ).ready(function() {
    console.log( "ready!" );
});

$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});