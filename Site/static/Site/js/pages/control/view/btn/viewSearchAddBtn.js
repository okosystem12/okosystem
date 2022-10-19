import {componentsData} from "../../componentsData";
import {newItem} from "../panel/search/event/newItem";

export const viewSearchAddBtn = () =>
    componentsData.viewSearchAddBtn.on('click', newItem);