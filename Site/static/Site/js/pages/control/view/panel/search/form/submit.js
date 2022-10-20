import {add} from "../../../../../../req/control/social/add";

export const submit = (form, e) => {
    e.preventDefault();
    const value = $(form).find('input[name=socialValue]').val();
    console.log(value);
    add({value}, (msg) => {
            console.log(msg)
    });
};