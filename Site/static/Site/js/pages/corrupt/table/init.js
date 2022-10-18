import {table as getCorruptTable} from "../../../req/corrupt/table";
import {make} from "./make";
import {table} from "../../../storage/corrupt/table";


export const init = () =>
    getCorruptTable((msg) => {
        table.setTable(msg);
        make();
    });