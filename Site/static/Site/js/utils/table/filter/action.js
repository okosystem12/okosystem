import {filterListToString} from "../../list/filterListToString";

export const action = (dt, options) => {
    dt.state.clear().destroy();
    options.destroyCallback(`${options.ajaxUrl}?data=${filterListToString(options.table.filter)}`);
};