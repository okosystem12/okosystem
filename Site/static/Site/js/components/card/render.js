import {render as globalRender} from "../../utils/render/render";

export const render = (render) => {
    switch (render?.type) {
        case 'date':
            return (data) => new Date(data).toLocaleDateString('ru');
        case 'datetime':
            return (data) => new Date(data).toLocaleString('ru');
        default:
            return globalRender(render)

    }
};