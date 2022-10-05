import {vchList} from "../../../../../storage/app/vchList";

import {remove as reqRemove} from "../../../../../req/config/vch/remove";
import {removeRowById} from "../../../../../table/handler/removeRowById";
import {table} from "../../../../../storage/config/vch/table";


export const remove = (id) => {
    vchList.remove('id', id);
    reqRemove({id});
    removeRowById(table.value.table, id);
};