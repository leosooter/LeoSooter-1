$($(document).ready(function() {
  console.log("Jquery has loaded");
  var valid = true;
  //Checks to see if inputs with class "required" have a value greater than 1 whenever
  //a input is focused or unfocused. Enables submit button if all have value greater than 1
  //At this point there is only 1 required field but I wanted to design the validation to check any that get added.
  $('.form-control').focusin(function(event) {
    console.log("changed");
    $(".required").each(function(){
      console.log($(this).val().length);
      if($(this).val().length === 0){
        valid = false;
      }
    });
    console.log(valid);
    if(valid){
      $(".form-button").prop('disabled', false);
    }
    else{
      $(".form-button").prop('disabled', true);
    }
    valid = true;
  });

  $('.form-control').focusout(function(event) {
    console.log("changed");
    $(".required").each(function(){
      console.log($(this).val().length);
      if($(this).val().length === 0){
        console.log();
        valid = false;
      }
    });
    console.log(valid);
    if(valid){
      $(".form-button").prop('disabled', false);
    }
    else{
      $(".form-button").prop('disabled', true);
    }
    valid = true;
  });

  $("#over-ride").click(function(){
    $(".form-button").prop('disabled', false);
  });

}));
