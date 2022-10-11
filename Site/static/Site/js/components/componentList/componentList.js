import {item} from "./item/item";
import {event as itemEvent} from "./item/event";

import {add} from "./add/add";
import {event as addEvent} from "./add/event";

export const componentList = (elem = null, list = [], limit = 0) => {
    if (elem !== null) {
        elem.addClass('component');
        elem.html(`<div class="component__place"></div>`);
        list.slice(0, limit === 0 ? list.length : limit).forEach(el => elem.find('.component__place').append(item(el)));
        elem.append(add());
        itemEvent(elem, limit);
        addEvent(elem, limit)
    }
};