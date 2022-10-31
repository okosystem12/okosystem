import {componentsData} from "../componentsData";
import {table} from "../../../storage/archive/table";
import {makeTable} from "../../../utils/table/makeTable";
import {view} from "./callback/view";


export const make = () => {
    componentsData.archiveTable.html('<table class="table table-striped table-bordered" width="100%"></table>');
    table.value['table'] = makeTable(
        componentsData.archiveTable.find('.table'),
        {
            table: table.value,
            ajax: {
                "url": "/archive/table/",
                "dataSrc": "data"
            },
            btnList: ['view'],
            destroyCallback: make,
            viewCallback: view,
        }
    );
};