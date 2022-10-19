import {componentsData} from "../../componentsData";
import {analysis} from "../../status/analysis";

export const btnViewAnalysisEvent= () =>
    componentsData.viewAnalysisBtn.on('click', analysis);