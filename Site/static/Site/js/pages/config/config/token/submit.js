import {componentsData} from "../componentsData";
import {work} from "../../../../req/config/token/work";
import {highlight} from "../../../../utils/form/highlight";

export const submit = (form, e) => {
    e.preventDefault();
    const {tokenInput} = componentsData;
    console.log(tokenInput);
    work({
        tokenVK: tokenInput.val().trim(),
    }, (msg) => {
        if (!msg.successText) {
            highlight(tokenInput, msg.errorHighlight);
        }
    });
};