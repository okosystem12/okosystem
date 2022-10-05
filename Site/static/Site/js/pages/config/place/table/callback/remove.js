import {info} from "../../../../../storage/config/place/info";
import {showNotificationDanger} from "../../../../../utils/notification/showNotificationDanger";
import {remove as countryRemove} from "../../form/country/remove";
import {remove as regionRemove} from "../../form/region/remove";
import {remove as cityRemove} from "../../form/city/remove";
import {countriesList} from "../../../../../storage/app/countriesList";
import {prepInfo} from "../prepInfo";
import {init} from "../init";
import {regionsList} from "../../../../../storage/app/regionsList";
import {citiesList} from "../../../../../storage/app/citiesList";


const callback = (dataList = null, id = null) => {
    dataList?.remove('id', id);
    prepInfo();
    init();
};

export const remove = (id) => {

    const row = info.value.find(el => el.id === id);

    if (row) {
        switch (row.typeRow) {
            case 'country':
                countryRemove({id: row.realId}, () => callback(countriesList, row.realId));
                break;
            case 'region':
                regionRemove({id: row.realId},  () => callback(regionsList, row.realId));
                break;
            case 'city':
                cityRemove({id: row.realId},  () => callback(citiesList, row.realId));
                break;
            default:
                showNotificationDanger('Ошибка определения типа записи');
                break;
        }

    }
};