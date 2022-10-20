import {componentsData} from "../../../../componentsData";

export const remove = (e) => {
    const {viewSearchAdd} = componentsData;
    viewSearchAdd.find(`.social-item[data-social="${e.currentTarget.dataset.social}"]`).remove();
};