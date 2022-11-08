import {componentsData} from "../../componentsData";
import {elem as statisticsElem} from "../../../../components/statistics/elem";
import {row as statisticsRow} from "../../../../components/statistics/row";

const filHelper = (controlUserList = []) => {

    const {statisticsControlUser} = componentsData;

    controlUserList.forEach(el => {
        if (el.subList) {
            statisticsControlUser.append(statisticsRow(el));
            filHelper(el.subList);
        }
        else {
            statisticsControlUser.append(statisticsElem(el));
        }

    });
};

export const fill = (controlUserList = []) => {
    const {statisticsControlUser} = componentsData;

    statisticsControlUser.html('');

    filHelper(controlUserList);
};