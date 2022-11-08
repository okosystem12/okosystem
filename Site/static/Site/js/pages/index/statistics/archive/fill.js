import {componentsData} from "../../componentsData";
import {filHelper} from "../filHelper";

export const fill = (archiveList = []) => {
    const {statisticsArchive} = componentsData;
    statisticsArchive.html('');
    filHelper(statisticsArchive, archiveList);
};