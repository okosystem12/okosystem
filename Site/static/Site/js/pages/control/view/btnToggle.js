import {componentsData} from "../componentsData";

export const btnToggle = (data = {}) => {
    const {viewSearch} = componentsData;

    viewSearch.removeAttr('disabled');

    console.log(data);
    console.log(data?.status?.blockSearch);

    if (data?.status?.blockSearch) {
        viewSearch.attr('disabled', 'disabled');
    }
};