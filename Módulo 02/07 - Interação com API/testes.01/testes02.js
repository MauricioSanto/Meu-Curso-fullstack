$( document ).ready(function() {

    // Toggle Debug Classes
    $("button").click( function() {
      
      var thisButton = $(this);
      var c_container = thisButton.parent().find('.container');
      var c_wrapper = thisButton.parent().find('.wrapper');
      var c_module = thisButton.parent().find('.module');
      var c_label = thisButton.parent().find('.label');
      
      c_container.toggleClass('debug');
      c_wrapper.toggleClass('debug');
      c_module.toggleClass('debug');
      
      c_label.each( function() {
          $(this).toggleClass('debug');
      });
      
    });
    
  });