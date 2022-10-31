import {componentsData} from "../componentsData";
import {table} from "../../../../storage/config/vch/table";
import {makeTable} from "../../../../utils/table/makeTable";
import {remove} from "./callback/remove";
import {edit} from "./callback/edit";


export const make = () => {
    componentsData.vchTable.html('<table class="table table-striped table-bordered" width="100%"></table>');
    table.value['table'] = makeTable(
        componentsData.vchTable.find('.table'),
        {
            table: table.value,
            ajax: {
                "url": "/config/vch/table/",
                "dataSrc": "data"
            },
            btnList: ['edit', 'remove'],
            destroyCallback: make,
            removeCallback: remove,
            editCallback: edit,
        }
    );
};