import {userFullName} from "../../utils/user/userFullName";
import {userShortName} from "../../utils/user/userShortName";
import {bDate} from "../../utils/date/bDate";
import {phoneList} from "../../storage/control/phoneList";
import {mailList} from "../../storage/control/mailList";
import {placeList} from "../../storage/app/placeList";
import {countriesList} from "../../storage/app/countriesList";
import {regionsList} from "../../storage/app/regionsList";
import {citiesList} from "../../storage/app/citiesList";

export const prepControlUserList = (table, controlUserList) => {

    const columnsObj = {};

    table.columnsList.map(column => columnsObj[column.data] = '');

    let result = [];
    for(let i = 0; i < 10000; i++){
       result =  result.concat(controlUserList);
    }

    return result.map(controlUser => {
        return {
            ...columnsObj,
            ...controlUser,
            fullName: userShortName(controlUser),
            birthDate: bDate(controlUser),

            phoneList: phoneList.value.filter(el => el.controlUser_id === controlUser.id),
            mailList: mailList.value.filter(el => el.controlUser_id === controlUser.id),
            birthPlace: placeDisassemble(controlUser.birthPlace_id),
            livePlace: placeDisassemble(controlUser.livePlace_id),
        }
    });
};

const placeDisassemble = (id = null) => {

    const result = [];
    const place = placeList.value.find(el => el.id === id);

    if (place) {
        const country = countriesList.value.find(el => el.id === place.country_id);
        const region = regionsList.value.find(el => el.id === place.region_id);
        const city = citiesList.value.find(el => el.id === place.city_id);

        result.push(country ? `${country.title}` : null);
        result.push(region ? `рег. ${region.title}` : null);
        result.push(city ? `г. ${city.title}` : null);
    }

    return result;
};