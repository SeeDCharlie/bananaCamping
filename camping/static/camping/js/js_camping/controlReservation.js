$(function() {
    var dateOne = new Date();
    var dateTow = new Date();
    dateTow.setDate(dateTow.getDate() + 1);
    $('input[name="daterangeReser"]').daterangepicker({



        timePicker: true,
        minDate: new Date(),
        locale: {
          format: 'MM/DD hh:mm A'
        },
        startDate:dateOne,
        endDate:dateTow,

    });
});



