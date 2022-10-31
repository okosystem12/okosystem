import {table} from "../../../../../storage/config/place/table";
import {hide} from "../../../../../utils/modal/hide";
import {componentsData} from "../../componentsData";

export const close = () => {
    table.value.table.ajax.reload(false);
    hide(componentsData.regionModal);
};