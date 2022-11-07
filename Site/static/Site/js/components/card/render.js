import {render as globalRender} from "../../utils/render/render";
import {dateFormat} from "../../utils/date/dateFormat";

export const render = (render) => {
    switch (render?.type) {
        case 'date':
            return (data) => new Date(data).toLocaleDateString('ru');
        case 'datetime':
            return (data) => dateFormat(data);
        default:
            return globalRender(render)

    }
};