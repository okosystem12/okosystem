import {table as getVchTable} from "../../../../req/config/vch/table";
import {make} from "./make";
import {table} from "../../../../storage/config/vch/table";


export const init = () =>
    getVchTable((msg) => {
        table.value = {
            columnsList: msg.columnsList,
            renderList: msg.renderList,
            patternList: msg.patternList,
            patternColumnsList: msg.patternColumnsList
        };

        make();
    });