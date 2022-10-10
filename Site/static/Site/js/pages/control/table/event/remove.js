import {remove as reqRemove} from "../../../../req/control/remove";
import {table} from "../../../../storage/control/table";

export const remove = (id) => {
    reqRemove({id}, () => {
        table.value.table.ajax.reload(false);
    });
};