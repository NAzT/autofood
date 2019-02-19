$(function() {
  $('#btn-1-1').click(function() {
    $.get('motor1?q=1', function(ret) {
      M.toast({html: ret});
    });
  });
  $('#btn-1-2').click(function() {
    $.get('motor1?q=2', function(ret) {
      M.toast({html: ret});
    });
  });
  $('#btn-1-3').click(function() {
    $.get('motor1?q=3', function(ret) {
      M.toast({html: ret});
    });
  });

  $('#btn-2-1').click(function() {
    $.get('motor2?q=1', function(ret) {
      M.toast({html: ret});
    });
  });
  $('#btn-2-2').click(function() {
    $.get('motor2?q=2', function(ret) {
      M.toast({html: ret});
    });
  });
  $('#btn-2-3').click(function() {
    $.get('motor2?q=3', function(ret) {
      M.toast({html: ret});
    });
  });

  $('#btn-3').click(function() {
    $.get('motor3', function(ret) {
      M.toast({html: ret});
    });
  });
});
