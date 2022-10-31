import {close} from "../../../close";
import {table} from "../../../../../../storage/control/table";
import {view} from "../../../../table/event/view";

export const response = (msg) => {
    if(msg.reloadTable){
        table.value.table.ajax.reload(false);
    }
    close();
    view(msg.userId);
};