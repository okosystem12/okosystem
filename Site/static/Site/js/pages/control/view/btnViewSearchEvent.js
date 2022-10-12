import {componentsData} from "../componentsData";
import {search} from "../status/search";

export const btnViewSearchEvent = () =>
    componentsData.viewSearch.on('click', () => search());