import {render} from "./render";

export const prepColumnsList = (table) => table.columnsList.map(el => {
    const _render = table.renderList.find(r => r.id === el.render_id);
    return {
        ...el,
        render: render(_render),
        className: el.hide ? 'noVis' : '',
    }
});