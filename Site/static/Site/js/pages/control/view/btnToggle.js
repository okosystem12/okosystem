import {componentsData} from "../componentsData";

export const btnToggle = (data = {}) => {
    const {viewSearchBtn, viewAnalysisBtn} = componentsData;

    viewSearchBtn.attr('disabled', 'disabled');
    viewAnalysisBtn.attr('disabled', 'disabled');


    if (!data?.status?.block) {
        viewSearchBtn.removeAttr('disabled');
        viewAnalysisBtn.removeAttr('disabled');
    }
};