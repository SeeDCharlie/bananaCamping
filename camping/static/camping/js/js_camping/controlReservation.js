$(function () {
  var dateOne = new Date();
  var dateTow = new Date();
  dateTow.setDate(dateTow.getDate() + 1);


  $('#fechaLlegada').text(formatDate(dateOne));

  $('#fechaSalida').text(formatDate(dateTow));

  
  $('#daterangeReser').daterangepicker({



    timePicker: true,
    minDate: new Date(),
    locale: {
      format: 'MM/DD hh:mm A'
    },
    startDate: dateOne,
    endDate: dateTow,

  });


  $('#daterangeReser').on('apply.daterangepicker', function (ev, picker) {
    $('#fechaLlegada').text(formatDate(new Date(picker.startDate)));
    $('#fechaSalida').text(formatDate(new Date(picker.endDate)));


  });

  function addZero(i) {
    if (i < 10) {
      i = "0" + i;
    }
    return i;
  }

  function formatDate(d) {
    var month = '' + (addZero(d.getMonth() + 1)),
    day = '' + addZero(d.getDate());

    return [ month, day,].join('-') + " a las " + formatAMPM(d);
  }

  function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
  }

});



