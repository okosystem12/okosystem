import {componentItem} from "./componentItem";
import {componentItemEvent} from "./componentItemEvent";
import {componentAddShow} from "./componentAddShow";

export const componentAddEvent = (elem = null, limit = 0) => {
    if (elem !== null) {
        $(elem).find('.component__add').unbind('click').click((e) => {
            const place = $(elem).find('.component__place');
            const item = $(place).find('.component__item');

            if (limit !== 0 && limit <= item.length) {
                return;
            }
            $(place).append(componentItem());
            componentItemEvent(elem, limit);
            componentAddShow(elem, !(limit !== 0 && limit <= item.length + 1));
        })
    }
};