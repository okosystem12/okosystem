import {add} from "../../../../../../req/control/social/add";
import {response} from "../event/response";
import {socialPrefix} from "../../../../../../var/socialPrefix";
import {highlight} from "../../../../../../utils/form/highlight";

export const submit = (form, e) => {
    e.preventDefault();

    const input = $(form).find('input[name=socialValue]');
    const value = input.val().replace(new RegExp(socialPrefix), '');

    add(value, (msg) => {
        if (msg.socialList) {
            response(msg);
        }
        else {
            highlight(input, msg.errorHighlight);
        }
    });
};