import {info as getPlaceInfo} from "../../req/config/place/info";
import {countriesList} from "../../storage/app/countriesList";
import {regionsList} from "../../storage/app/regionsList";

export const placeInfo = () =>
    getPlaceInfo({}, (msg) => {
        countriesList.value = msg.countriesList;
        regionsList.value = msg.regionsList;
    });