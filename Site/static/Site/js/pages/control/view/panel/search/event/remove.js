import {componentsData} from "../../../../componentsData";

export const remove = (e) => {
    const {viewSearch} = componentsData;
    viewSearch.find(`.social-item[data-social="${e.currentTarget.dataset.social}"]`).remove();
};