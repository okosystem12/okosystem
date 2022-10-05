import {componentItem} from "./componentItem";
import {componentItemEvent} from "./componentItemEvent";

import {componentAdd} from "./componentAdd";
import {componentAddEvent} from "./componentAddEvent";

export const componentList = (elem = null, list = [], limit = 0) => {
    if (elem !== null) {
        elem.html(`<div class="component__place"></div>`);
        elem.addClass('component');
        list.slice(0, limit === 0 ? list.length : limit).forEach(el => elem.find('.component__place').append(componentItem(el)));
        componentItemEvent(elem, limit);
        elem.append(componentAdd());
        componentAddEvent(elem, limit)
    }
};