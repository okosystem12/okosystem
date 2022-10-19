import {componentsData} from "../../../componentsData";
import {remove} from "./event/remove";

export const makeAddEvent = () => {
    const {viewSearch} = componentsData;
    const sList = viewSearch.find('.social-item');
    if (sList.length) {
        console.log(sList);
        const item = sList[sList.length - 1];
        $(item).find('.social-item__remove').off('click').on('click', remove);
    }
};