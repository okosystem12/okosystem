import {componentsData} from "../../../componentsData";
import {reject} from "./event/reject";
import {confirm} from "./event/confirm";

export const makeBtnEvent = () => {
    const {viewAnalysis} = componentsData;
    const sList = viewAnalysis.find('.corrupt__control');
    sList.map(sl => {
        $(sList[sl]).find('.corrupt__reject').off('click').on('click', reject);
        $(sList[sl]).find('.corrupt__confirm').off('click').on('click', confirm);
    });
};