import {render} from "./render";

export const prepColumnsList = (table) => table.columnsList.map(el => {
    return {
        ...el,
        render: render(table.renderList.find(r => r.id === el.render_id)),
        className: el.hide ? 'noVis' : '',
    }
});