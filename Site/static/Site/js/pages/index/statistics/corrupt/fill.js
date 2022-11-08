import {componentsData} from "../../componentsData";
import {filHelper} from "../filHelper";


export const fill = (corruptList = []) => {
    const {statisticsCorrupt} = componentsData;
    statisticsCorrupt.html('');
    filHelper(statisticsCorrupt, corruptList);
};