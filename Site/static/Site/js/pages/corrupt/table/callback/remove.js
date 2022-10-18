import {remove as reqRemove} from "../../../../req/corrupt/remove";
import {table} from "../../../../storage/corrupt/table";

export const remove = (id) =>
    reqRemove({id}, () => {
        table.value.table.ajax.reload(false);
    });