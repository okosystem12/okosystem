import {show} from "../add/show";

export const event = (elem = null, limit = 0) => {
    if(elem !== null) {

        const componentItemList = $(elem).find('.component__item');

       componentItemList.map(el => {
           const item = $(componentItemList[el]);
            item.find('.component__remove').unbind('click').click((e) => {
                item.remove();
                show(elem, !(limit !== 0 && limit <= componentItemList.length - 1));
            });
        });
    }
};