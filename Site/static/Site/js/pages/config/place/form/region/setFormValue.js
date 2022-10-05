import {componentsData} from "../../componentsData";
import {editId} from "../../../../../storage/config/place/editId";
import {initChosen} from "../../../../../utils/list/initChosen";
import {optionList} from "../../../../../components/select/optionList";
import {countriesList} from "../../../../../storage/app/countriesList";
import {label} from "../../../../../utils/modal/label";

export const setFormValue = (data = {}) => {
    editId.value = data.realId || null;
    const {regionName, regionCountry, regionModalLabel} = componentsData;

    label(regionModalLabel, editId.value, 'регион', data.region);

    regionName.val(data.region || '');

    regionCountry.html(optionList(countriesList.value));
    regionCountry.val(data.country_id || '');
    initChosen(regionCountry);
};