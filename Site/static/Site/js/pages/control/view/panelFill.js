import {search} from "./panel/search";
import {archive} from "./panel/archive";
import {analysis} from "./panel/analysis";

export const panelFill = (data = {}) => {
    search(data);
    analysis(data);
    archive(data);
};