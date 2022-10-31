import {render} from "./render";

export const prepColumnsList = (table) => table.columnsList.map(el => {
    const className = [];

    if(el.hide){
        className.push('noVis')
    }

    if(!el.searchable){
        className.push('noHighlight')
    }

    return {
        ...el,
        render: render(table.renderList.find(r => r.id === el.render_id)),
        className:  className.join(' '),
    }
});