import {componentsData} from "../componentsData";
import {table} from "../../../../storage/config/place/table";
import {makeTable} from "../../../../utils/table/makeTable";
import {edit} from "./callback/edit";
import {remove} from "./callback/remove";
import {filter} from "./filter/filter";
import {table as tableElem} from "../../../../components/table/table";


const ajaxUrl = "/config/place/table/";

export const make = (url = ajaxUrl) => {
    componentsData.placeTable.html(tableElem());
    table.value['table'] = makeTable(
        componentsData.placeTable.find('.table'),
        {
            table: table.value,
            ajaxUrl,
            ajax: {
                "url": url,
                "dataSrc": "data"
            },
            filter: filter(table.value),
            filterInfo: componentsData.placeTable.find('.filter-info'),
            btnList: ['edit', 'remove'],
            destroyCallback: make,
            removeCallback: remove,
            editCallback: edit,
        }
    );
};