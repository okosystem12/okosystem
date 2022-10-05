import {componentsData} from "../../componentsData";
import {editId} from "../../../../../storage/config/place/editId";
import {label} from "../../../../../utils/modal/label";

export const setFormValue = (data = {}) => {
    editId.value = data.realId || null;
    const {countryName, countryModalLabel} = componentsData;

    label(countryModalLabel, editId.value, 'страну', data.country);

    countryName.val(data.country || '');
};