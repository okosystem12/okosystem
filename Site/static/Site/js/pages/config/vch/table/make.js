import {componentsData} from "../componentsData";
import {table} from "../../../../storage/config/vch/table";
import {makeTable} from "../../../../table/makeTable";
import {remove} from "./callback/remove";
import {edit} from "./callback/edit";


export const make = () => {
    componentsData.placeTable.html('<table class="table table-striped table-bordered" width="100%"></table>');
    table.value['table'] = makeTable(
        componentsData.placeTable.find('.table'),
        {
            table: table.value,
            btnList: ['edit', 'remove'],
            destroyCallback: make,
            removeCallback: remove,
            editCallback: edit,
        }
    );
};