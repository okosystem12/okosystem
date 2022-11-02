import {componentsData} from "../componentsData";
import {table} from "../../../storage/archive/table";
import {makeTable} from "../../../utils/table/makeTable";
import {view} from "./callback/view";
import {remove} from "./callback/remove";
import {table as tableElem} from "../../../components/table/table";
import {filter} from "./filter/filter";

const ajaxUrl = "/archive/table/";

export const make = (url = ajaxUrl) => {
    componentsData.archiveTable.html(tableElem());
    table.value['table'] = makeTable(
        componentsData.archiveTable.find('.table'),
        {
            table: table.value,
            ajaxUrl,
            ajax: {
                url: url,
                dataSrc: "data"
            },
            btnList: ['remove'],
            filter: filter(table.value),
            filterInfo: componentsData.archiveTable.find('.filter-info'),
            destroyCallback: make,
            viewCallback: view,
            removeCallback: remove,
        }
    );
};