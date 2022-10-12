import {componentsData} from "../componentsData";

export const btnToggle = (data = {}) => {
    const {viewSearch, viewAnalysis} = componentsData;

    viewSearch.removeAttr('disabled');
    viewAnalysis.removeAttr('disabled');


    if (data?.status?.blockSearch) {
        viewSearch.attr('disabled', 'disabled');
    }


    if (data?.status?.blockAnalysis) {
        viewAnalysis.attr('disabled', 'disabled');
    }
};