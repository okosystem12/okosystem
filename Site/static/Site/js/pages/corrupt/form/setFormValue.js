import {componentsData} from "../componentsData";
import {editId} from "../../../storage/corrupt/editId";
import {label} from "../../../utils/modal/label";

export const setFormValue = (data = {}) => {
    editId.value = data.id || null;
    const {corruptValue, corruptInfo, corruptModalLabel} = componentsData;

    label(corruptModalLabel, editId.value, 'ключевое слово', data.value);

    corruptValue.val(data.value || '');
    corruptInfo.val(data.info || '');
};