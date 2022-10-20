import {componentsData} from "../../../componentsData";
import {remove} from "./event/remove";
import {validate} from "./form/validate";

export const makeAddEvent = () => {
    const {viewSearchAdd} = componentsData;
    const sList = viewSearchAdd.find('.social-item');
    if (sList.length) {
        console.log(sList);
        const item = sList[sList.length - 1];
        $(item).find('.social-item__remove').off('click').on('click', remove);
        $(item).find('.social-item__add').off('click').on('click', () => validate(item));
    }
};