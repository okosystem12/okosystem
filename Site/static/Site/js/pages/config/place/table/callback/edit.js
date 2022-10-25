import {info} from "../../../../../storage/config/place/info";
import {openForm as countryForm} from "../../form/country/openForm";
import {openForm as regionForm} from "../../form/region/openForm";
import {openForm as cityForm} from "../../form/city/openForm";
import {showNotificationDanger} from "../../../../../utils/notification/showNotificationDanger";
import {get} from "../../../../../req/config/place/contries/get";

export const edit = (id) => {
    get({id}, (msg) => {
        console.log(msg);
    });

    const row = info.value.find(el => el.id === id);

    if (row) {
        switch (row.typeRow) {
            case 'country':
                countryForm(row);
                break;
            case 'region':
                regionForm(row);
                break;
            case 'city':
                cityForm(row);
                break;
            default:
                showNotificationDanger('Ошибка');
                break;
        }

    }
};