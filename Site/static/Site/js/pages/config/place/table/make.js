import {componentsData} from "../componentsData";
import {table} from "../../../../storage/config/place/table";
import {makeTable} from "../../../../utils/table/makeTable";
import {rowsAdd} from "../../../../utils/table/handler/rowsAdd";
import {info} from "../../../../storage/config/place/info";
import {edit} from "./callback/edit";
import {remove} from "./callback/remove";


export const make = () => {
    componentsData.placeTable.html('<table class="table table-striped table-bordered" width="100%"></table>');
    table.value['table'] = makeTable(
        componentsData.placeTable.find('.table'),
        {
            table: table.value,
            ajax: {
                "url": "/config/place/table/",
                "dataSrc": "data"
            },
            btnList: ['edit', 'remove'],
            destroyCallback: make,
            removeCallback: remove,
            editCallback: edit,
        }
    );
    rowsAdd(table.value.table, info.value, false, false);
};