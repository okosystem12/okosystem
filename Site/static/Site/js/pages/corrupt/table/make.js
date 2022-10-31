import {componentsData} from "../componentsData";
import {table} from "../../../storage/corrupt/table";
import {makeTable} from "../../../utils/table/makeTable";
import {remove} from "./callback/remove";
import {edit} from "./callback/edit";


export const make = () => {
    componentsData.corruptTable.html('<table class="table table-striped table-bordered" width="100%"></table>');
    table.value['table'] = makeTable(
        componentsData.corruptTable.find('.table'),
        {
            table: table.value,
            ajax: {
                url: `/corrupt/table/`,
                dataSrc: "data"
            },
            btnList: ['edit', 'remove'],
            filter: [{
                text: 'remove',
                action: (e, dt, node, config) => {
                    dt.state.clear().destroy();
                    make();
                    dt.ajax.url(`/corrupt/table/?id=1`);
                    dt.ajax.reload(false);
                }
            },],
            destroyCallback: make,
            removeCallback: remove,
            editCallback: edit,
        }
    );
};