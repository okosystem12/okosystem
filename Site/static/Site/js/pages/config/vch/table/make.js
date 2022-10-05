import {componentsData} from "../componentsData";
import {table} from "../../../../storage/config/vch/table";
import {makeTable} from "../../../../table/makeTable";
import {rowsAdd} from "../../../../table/handler/rowsAdd";
import {vchList} from "../../../../storage/app/vchList";
import {vchInfo} from "../../../app/vchInfo";
import {remove} from "./callback/remove";
import {edit} from "./callback/edit";


export const make = () => {
    componentsData.placeTable.html('<table class="table table-striped table-bordered" width="100%"></table>');
    table.value['table'] = makeTable(
        componentsData.placeTable.find('.table'),
        {
            table: table.value,
            btnList: ['edit', 'remove'],
            destroyCallback: vchInfo,
            refreshCallback: vchInfo,
            removeCallback: remove,
            editCallback: edit,
        }
    );
    rowsAdd(table.value.table, vchList.value, false, false);
};