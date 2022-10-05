import {table as getPlaceTable} from "../../../../req/config/place/table";
import {make} from "./make";
import {table} from "../../../../storage/config/place/table";


export const init = () =>
    getPlaceTable((msg) => {
        table.value = {
            columnsList: msg.columnsList,
            renderList: msg.renderList,
            patternList: msg.patternList,
            patternColumnsList: msg.patternColumnsList
        };
        make();
    });