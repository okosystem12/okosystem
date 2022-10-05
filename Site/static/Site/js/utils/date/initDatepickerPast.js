import {initDatepicker} from "./initDatepicker";

export const initDatepickerPast = (elem) => {
    initDatepicker(elem);
    $(elem).datepicker("option", "maxDate", new Date());
};