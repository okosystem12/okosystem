import {item} from "../item/item";
import {event as itemEvent} from "../item/event";
import {show} from "./show";

export const event = (elem = null, limit = 0) => {
    if (elem !== null) {
        $(elem).find('.component__add').unbind('click').click((e) => {
            const place = $(elem).find('.component__place');
            const itemList = $(place).find('.component__item');

            if (limit !== 0 && limit <= item.length) {
                return;
            }
            $(place).append(item());
            itemEvent(elem, limit);
            show(elem, !(limit !== 0 && limit <= itemList.length + 1));
        })
    }
};