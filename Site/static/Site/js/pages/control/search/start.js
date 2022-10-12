import {start as startSearch} from "../../../req/control/search/start";
import {userId} from "../../../storage/control/userId";
import {table} from "../../../storage/control/table";

export const start = () =>
    startSearch({id: userId.value}, ()=>{
        table.value.table.ajax.reload(false);
    });