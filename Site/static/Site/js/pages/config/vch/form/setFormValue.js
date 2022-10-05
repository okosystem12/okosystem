import {componentsData} from "../componentsData";
import {editId} from "../../../../storage/config/vch/editId";
import {label} from "../../../../utils/modal/label";

export const setFormValue = (data = {}) => {
    editId.value = data.id || null;
    const {vchNumber, vchModalLabel} = componentsData;

    label(vchModalLabel, editId.value, 'ВЧ', data.number);

    vchNumber.val(data.number || '');
};