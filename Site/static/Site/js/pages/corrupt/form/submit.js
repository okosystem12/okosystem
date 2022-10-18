import {componentsData} from "../componentsData";
import {work} from "../../../req/corrupt/work";
import {editId} from "../../../storage/corrupt/editId";
import {highlight} from "../../../utils/form/highlight";
import {close} from "./close";

export const submit = (form, e) => {
    e.preventDefault();
    const {corruptValue, corruptInfo} = componentsData;

    work({
        id: editId.value,
        value: corruptValue.val().trim(),
        info: corruptInfo.val().trim(),
    }, (msg) => {
        if (msg.successText) {
            close();
        }
        else {
            highlight(corruptValue);
        }
    });
};