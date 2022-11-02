import {table} from "../../../../../../storage/control/table";
import {corruptList} from "../../../../../../storage/control/corruptList";
import {setViewValue} from "../../../setViewValue";

export const response = (msg) => {
    if(msg.reloadTable){
        table.value.table.ajax.reload(false);
    }

    corruptList.value = msg.corruptList;
    setViewValue(msg.controlUser[0]);
};