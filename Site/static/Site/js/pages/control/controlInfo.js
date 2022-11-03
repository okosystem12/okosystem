import {info as getControlInfo} from "../../req/control/info";
import {countriesList} from "../../storage/app/countriesList";
import {regionsList} from "../../storage/app/regionsList";
import {citiesList} from "../../storage/app/citiesList";
import {vchList} from "../../storage/app/vchList";
import {statusList} from "../../storage/control/statusList";

export const controlInfo = () =>
    getControlInfo((msg) => {
        countriesList.value = msg.countriesList;
        regionsList.value = msg.regionsList;
        citiesList.value = msg.citiesList;
        vchList.value = msg.vchList;
        statusList.value = msg.statusList;
    });