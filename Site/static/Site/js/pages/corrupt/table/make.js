import {componentsData} from "../componentsData";
import {table} from "../../../storage/corrupt/table";
import {makeTable} from "../../../utils/table/makeTable";
import {remove} from "./callback/remove";
import {edit} from "./callback/edit";
import {table as tableElem} from "../../../components/table/table";


const ajaxUrl = `/corrupt/table/`;

export const make = (url = ajaxUrl) => {
    componentsData.corruptTable.html(tableElem());
    table.value['table'] = makeTable(
        componentsData.corruptTable.find('.table'),
        {
            table: table.value,
            ajaxUrl,
            ajax: {
                url: url,
                dataSrc: "data"
            },
            btnList: ['edit', 'remove'],
            destroyCallback: make,
            removeCallback: remove,
            editCallback: edit,
        }
    );
};