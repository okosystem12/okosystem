import {componentsData} from "../../pages/config/vch/componentsData";
import {work} from "../../req/config/vch/work";
import {editId} from "../../storage/config/vch/editId";
import {highlight} from "../validate/handler/highlight";
import {removeRowById} from "../../table/handler/removeRowById";
import {table} from "../../storage/config/vch/table";
import {rowsAdd} from "../../table/handler/rowsAdd";
import {vchList} from "../../storage/app/vchList";
import {hide} from "../../utils/modal/hide";

export const vchForm = (form, e) => {
    e.preventDefault();
    const {vchNumber, vchModal} = componentsData;

    work({
        id: editId.value,
        number: vchNumber.val().trim(),
    }, (msg) => {
        if (msg.successText) {
            removeRowById(table.value.table,editId.value);
            vchList.remove('id', editId.value);
            vchList.pushList(msg.vchList);

            rowsAdd(table.value.table, msg.vchList, false, false);
            hide(vchModal);
        }
        else {
            highlight(vchNumber);
        }
    });
};