import {table as getControlTable} from "../../../req/control/table";
import {make} from "./make";
import {controlInfo} from "../controlInfo";
import {table} from "../../../storage/control/table";

export const init = () =>
    getControlTable((msg) => {
        table.setTable(msg);
        controlInfo();
        make();
    });