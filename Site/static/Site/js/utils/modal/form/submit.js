import {doNothing} from "../../doNothing";

export const submit = (form, e, callback = doNothing) => {
    e.preventDefault();
    const elem = $(form).find('.form-control');
    callback($.trim(elem.val()));
    $.fancybox.close();
};