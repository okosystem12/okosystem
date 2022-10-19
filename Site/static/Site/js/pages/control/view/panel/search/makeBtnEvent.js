import {componentsData} from "../../../componentsData";
import {reject} from "./event/reject";
import {confirm} from "./event/confirm";

export const makeBtnEvent = () => {
    const {viewSearch} = componentsData;
    const sList = viewSearch.find('.social-list');
    sList.map(sl => {
        $(sList[sl]).find('.social-list__reject').off('click').on('click', reject);
        $(sList[sl]).find('.social-list__confirm').off('click').on('click', confirm);
    });
};