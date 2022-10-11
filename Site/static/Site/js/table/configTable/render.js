import {render as globalRender} from "../../utils/render";

export const render = (render) => {
    switch (render?.type) {
        case 'date':
            return DataTable.render.date();
        case 'datetime':
            return DataTable.render.datetime();
        default:
            return globalRender(render)
    }
};