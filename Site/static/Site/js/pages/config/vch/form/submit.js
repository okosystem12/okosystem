import {componentsData} from "../componentsData";
import {work} from "../../../../req/config/vch/work";
import {editId} from "../../../../storage/config/vch/editId";
import {highlight} from "../../../../utils/form/highlight";
import {close} from "./close";

export const submit = (form, e) => {
    e.preventDefault();
    const {vchNumber} = componentsData;

    work({
        id: editId.value,
        number: vchNumber.val().trim(),
    }, (msg) => {
        if (msg.successText) {
            close();
        }
        else {
            highlight(vchNumber);
        }
    });
};