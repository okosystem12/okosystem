import {table} from "../../../../../../storage/control/table";
import {socialList} from "../../../../../../storage/control/socialList";
import {setViewValue} from "../../../setViewValue";

export const response = (msg) => {
    if (msg.reloadTable) {
        table.value.table.ajax.reload(false);
    }
    socialList.value = msg.socialList;
    setViewValue(msg.controlUser[0]);
};