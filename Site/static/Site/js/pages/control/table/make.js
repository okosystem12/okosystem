import {componentsData} from "../componentsData";
import {table} from "../../../storage/control/table";
import {makeTable} from "../../../utils/table/makeTable";
import {remove} from "./event/remove";
import {edit} from "./event/edit";
import {view} from "./event/view";
import {table as tableElem} from "../../../components/table/table";
import {filter} from "./filter/filter";


const ajaxUrl = "/control/table/";

export const make = (url = ajaxUrl) => {
    componentsData.controlTable.html(tableElem());
    table.value['table'] = makeTable(
        componentsData.controlTable.find('.table'),
        {
            table: table.value,
            ajaxUrl,
            ajax: {
                "url": url,
                "dataSrc": "data"
            },
            btnList: ['view', 'edit', 'remove'],
            filter: filter(table.value),
            filterInfo: componentsData.controlTable.find('.filter-info'),
            destroyCallback: make,
            removeCallback: remove,
            editCallback: edit,
            viewCallback: view,
        }
    );
};