import {componentsData} from "../componentsData";

export const btnToggle = (data = {}) => {
    const {viewSearchBtn, viewAnalysisBtn} = componentsData;

    // viewSearchBtn.attr('disabled', 'disabled');
    // viewAnalysisBtn.attr('disabled', 'disabled');


    if ((data?.status.stage === 'prepare' && data?.status.type !== 'search') || (data?.status.stage === 'work' && data?.status.type !== 'analysis')) {
        viewSearchBtn.removeAttr('disabled');
    }


    if (data?.status.stage === 'work' && data?.status.type !== 'analysis') {
        viewAnalysisBtn.removeAttr('disabled');
    }
};