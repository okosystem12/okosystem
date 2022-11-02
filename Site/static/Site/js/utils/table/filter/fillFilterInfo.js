import {objForEach} from "../../list/objForEach";
import {filterElem} from "../../../components/table/filterElem";

export const fillFilterInfo = (options = {}) => {
    if (options.filterInfo) {
        options.filterInfo.html('');

        objForEach(options.table.filter, (key) => {
            options.filterInfo.append(filterElem(options.table.filter[key]['title'], options.table.filter[key]['text']));
        });

    }
};