import {table as getVchTable} from "../../../../req/config/vch/table";
import {make} from "./make";
import {table} from "../../../../storage/config/vch/table";


export const init = () =>
    getVchTable((msg) => {
        table.setTable(msg);

        make();
    });