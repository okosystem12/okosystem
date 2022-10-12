import {table} from "../../../storage/control/table";
import {hide} from "../../../utils/modal/hide";
import {componentsData} from "../componentsData";

export const close = () => {
    table.value.table.ajax.reload(false);
    hide(componentsData.viewModal);
};