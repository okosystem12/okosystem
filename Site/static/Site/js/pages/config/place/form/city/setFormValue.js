import {componentsData} from "../../componentsData";
import {editId} from "../../../../../storage/config/place/editId";
import {countriesList} from "../../../../../storage/app/countriesList";
import {initOptionList} from "../../../../../components/select/initOptionList";
import {filterRegion} from "../../../../../utils/list/filter/filterRegion";
import {label} from "../../../../../utils/modal/label";

export const setFormValue = (data = {}) => {
    editId.value = data.realId || null;
    const {cityName, cityCountry, cityRegion, cityModalLabel} = componentsData;

    label(cityModalLabel, editId.value, 'город', data.city);

    cityName.val(data.city || '');

    initOptionList(cityCountry, countriesList.value, data.country_id);
    initOptionList(
        cityRegion,
        filterRegion(data.country_id ? parseInt(data.country_id) : null),
        data.region_id
    );

    cityCountry.unbind('change').change(() => {
        const value = cityRegion.val();
        initOptionList(
            cityRegion,
            filterRegion(parseInt(cityCountry.val())),
            value
        )
    })
};

