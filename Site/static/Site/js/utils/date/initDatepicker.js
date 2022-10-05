export const initDatepicker = (elem) => {
    elem
        .datepicker({
            dateFormat: "dd.mm.yy",
            changeYear: true,
            changeMonth: true,
            constrainInput: false,
            regional: 'ru',
            autoSize: true,
            showButtonPanel: true,
            yearRange: "-100:+10",
            closeText: 'Сбросить',
            onClose: (dateText, inst) => {
                if ($(window.event.srcElement).hasClass('ui-datepicker-close')) {
                    $.datepicker._clearDate(elem);
                }
            },
            onSelect: (dateText, inst) => {
               elem.keyup();
            }
        })
        .attr('readonly', 'readonly')
        .addClass('text-center')
        .unbind('keyup');
};