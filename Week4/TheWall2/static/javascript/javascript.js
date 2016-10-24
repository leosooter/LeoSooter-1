$($(document).ready(function() {
  console.log("Jquery has loaded");
  //$(".comment_form").hide();
  $(".show_comment_form").click(function(){
    $(this).siblings('.comment_form').toggle();
  });
  $(".show_delete").click(function(){
    $(this).hide();
    $(this).siblings('.delete_form').show();
  });
  $(".cancel_delete").click(function(){
    $(this).parent().hide();
    $(this).parent().siblings('.show_delete').show();
  });
}));
