import {componentsData} from "../componentsData";
import {start} from "../search/start";

export const btnViewSearchEvent = () =>
    componentsData.viewSearch.on('click', () => start());