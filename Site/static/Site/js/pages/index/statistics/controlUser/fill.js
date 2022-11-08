import {componentsData} from "../../componentsData";
import {filHelper} from "../filHelper";


export const fill = (controlUserList = []) => {
    const {statisticsControlUser} = componentsData;

    statisticsControlUser.html('');

    filHelper(statisticsControlUser, controlUserList);
};