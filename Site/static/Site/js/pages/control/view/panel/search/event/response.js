import {close} from "../../../close";
import {table} from "../../../../../../storage/control/table";

export const response = (msg) => {
    if(msg.closeModal){
        close()
    }
    else if(msg.reloadTable){
        table.value.table.ajax.reload(false);
    }
};