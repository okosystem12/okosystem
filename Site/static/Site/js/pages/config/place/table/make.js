import {componentsData} from "../componentsData";
import {table} from "../../../../storage/config/place/table";
import {makeTable} from "../../../../table/makeTable";
import {rowsAdd} from "../../../../table/handler/rowsAdd";
import {info} from "../../../../storage/config/place/info";
import {placeInfo} from "../../../app/placeInfo";
import {edit} from "./callback/edit";
import {remove} from "./callback/remove";


export const make = () => {
    componentsData.placeTable.html('<table class="table table-striped table-bordered" width="100%"></table>');
    table.value['table'] = makeTable(
        componentsData.placeTable.find('.table'),
        {
            table: table.value,
            btnList: ['edit', 'remove'],
            destroyCallback: placeInfo,
            refreshCallback: placeInfo,
            removeCallback: remove,
            editCallback: edit,
        }
    );
    rowsAdd(table.value.table, info.value, false, false);
};