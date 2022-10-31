import {showNotificationDanger} from "../../../../../utils/notification/showNotificationDanger";
import {remove as countryRemove} from "../../form/country/remove";
import {remove as regionRemove} from "../../form/region/remove";
import {remove as cityRemove} from "../../form/city/remove";
import {init} from "../init";
import {placeInfo} from "../../../../app/placeInfo";
import {table} from "../../../../../storage/config/place/table";


const callback = () => {
    placeInfo();
    init();
};

export const remove = (id) => {

    const row = table.value.table.row(`#${id}`).data();

    if (row) {
        switch (row.typeRow) {
            case 'country':
                countryRemove({id: row.realId}, callback);
                break;
            case 'region':
                regionRemove({id: row.realId},  callback);
                break;
            case 'city':
                cityRemove({id: row.realId},  callback);
                break;
            default:
                showNotificationDanger('Ошибка определения типа записи');
                break;
        }
    }
};