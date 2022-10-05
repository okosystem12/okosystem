import {componentsData} from "../componentsData";
import {table} from "../../../storage/control/table";
import {makeTable} from "../../../table/makeTable";
import {remove} from "./event/remove";
import {edit} from "./event/edit";
import {view} from "./event/view";
import {controlInfo} from "../controlInfo";

export const make = () => {
    componentsData.controlTable.html('<table class="table table-striped table-bordered" width="100%"></table>');
    table.value['table'] = makeTable(
        componentsData.controlTable.find('.table'),
        {
            table: table.value,
            btnList: ['view', 'edit', 'remove'],
            destroyCallback: () => {
                make();
                controlInfo();
            },
            refreshCallback: () => {
                controlInfo();
            },
            removeCallback: remove,
            editCallback: edit,
            viewCallback: view,
        }
    );
};