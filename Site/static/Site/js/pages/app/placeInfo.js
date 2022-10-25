import {info as getPlaceInfo} from "../../req/config/place/info";
import {countriesList} from "../../storage/app/countriesList";
import {regionsList} from "../../storage/app/regionsList";
import {citiesList} from "../../storage/app/citiesList";
import {prepInfo} from "../config/place/table/prepInfo";
import {init} from "../config/place/table/init";
import {type} from "../../storage/config/place/type";

export const placeInfo = () =>
    getPlaceInfo({type: type.value}, (msg) => {
        countriesList.value = msg.countriesList;
        regionsList.value = msg.regionsList;

        init();
    });