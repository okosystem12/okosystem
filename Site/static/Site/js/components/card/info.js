import {table} from "../../storage/control/table";
import {render} from "./render";

export const info = (control = {}) => {
    const columnList = table.value.columnsList.filter(el => el.view).sort((a, b) => a.viewOrder - b.viewOrder === 0 ? a.pk - b.pk : a.viewOrder - b.viewOrder);

    return `<div class="card-info">
${
        columnList.map(el => {
            const _val = control[el.data];
            if(_val !== '' && _val.length !== 0) {
            const _render = table.value.renderList.find(r => r.id === el.render_id);
                return `<div class="card-info__title">${el.title}</div><div class="card-info__value">${_render ? render(_render)(_val) : _val}</div>`
            }
            else {
                return null;
            }
        }).filter(el => el !== null).join('')
    }
</div>`;
};