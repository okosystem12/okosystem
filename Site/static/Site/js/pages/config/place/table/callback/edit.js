import {openForm as countryForm} from "../../form/country/openForm";
import {openForm as regionForm} from "../../form/region/openForm";
import {openForm as cityForm} from "../../form/city/openForm";
import {showNotificationDanger} from "../../../../../utils/notification/showNotificationDanger";
import {get as getCountries} from "../../../../../req/config/place/countries/get";
import {get as getRegions} from "../../../../../req/config/place/regions/get";
import {get as getCity} from "../../../../../req/config/place/city/get";
import {table} from "../../../../../storage/config/place/table";

export const edit = (id) => {

    const row = table.value.table.row(`#${id}`).data();

    if (row) {
        switch (row.typeRow) {
            case 'country':
                getCountries({id: row.realId}, (msg) => countryForm(msg.country[0]));
                break;
            case 'region':
                getRegions({id: row.realId}, (msg) => regionForm(msg.region[0]));
                break;
            case 'city':
                getCity({id: row.realId}, (msg) => cityForm(msg.city[0]));
                break;
            default:
                showNotificationDanger('Ошибка');
                break;
        }
    }
};