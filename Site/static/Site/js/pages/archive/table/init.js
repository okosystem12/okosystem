import {table as getArchiveTable} from "../../../req/archive/table";
import {make} from "./make";
import {table} from "../../../storage/archive/table";


export const init = () =>
    getArchiveTable((msg) => {
        table.setTable(msg);
        make();
    });