import {search} from "./panel/search";
import {analysis} from "./panel/analysis";

export const panelFill = (data = {}) => {
    search(data);
    analysis(data);
};