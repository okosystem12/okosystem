
import {remove as reqRemove} from "../../../../../req/config/vch/remove";
import {table} from "../../../../../storage/config/vch/table";

export const remove = (id) => {
    reqRemove({id}, () => {
        table.value.table.ajax.reload(false);
    });
};