import {componentsData} from "../componentsData";
import {table} from "../../../../storage/config/vch/table";
import {makeTable} from "../../../../utils/table/makeTable";
import {remove} from "./callback/remove";
import {edit} from "./callback/edit";
import {table as tableElem} from "../../../../components/table/table";

const ajaxUrl = "/config/vch/table/";

export const make = (url = ajaxUrl) => {
    componentsData.vchTable.html(tableElem());
    table.value['table'] = makeTable(
        componentsData.vchTable.find('.table'),
        {
            table: table.value,
            ajaxUrl,
            ajax: {
                "url": url,
                "dataSrc": "data"
            },
            btnList: ['edit', 'remove'],
            destroyCallback: make,
            removeCallback: remove,
            editCallback: edit,
        }
    );
};