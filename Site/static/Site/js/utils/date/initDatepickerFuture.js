import {initDatepicker} from "./initDatepicker";

export const initDatepickerFuture = (elem) => {
    initDatepicker(elem);
    $(elem).datepicker("option", "minDate", new Date());
};