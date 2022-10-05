import {info as getControlInfo} from "../../req/control/info";
import {rowsAdd} from "../../table/handler/rowsAdd";
import {fileList} from "../../storage/control/fileList";
import {controlUserImgList} from "../../storage/control/controlUserImgList";
import {controlUserList} from "../../storage/control/controlUserList";
import {mailList} from "../../storage/control/mailList";
import {phoneList} from "../../storage/control/phoneList";
import {table} from "../../storage/control/table";
import {prepControlUserList} from "./prepControlUserList";
import {countriesList} from "../../storage/app/countriesList";
import {regionsList} from "../../storage/app/regionsList";
import {citiesList} from "../../storage/app/citiesList";
import {placeList} from "../../storage/app/placeList";

export const controlInfo = (reset) =>
    getControlInfo((msg) => {
        controlUserList.value = msg.controlUserList;
        controlUserImgList.value = msg.controlUserImgList;
        fileList.value = msg.fileList;
        mailList.value = msg.mailList;
        phoneList.value = msg.phoneList;
        placeList.value = msg.placeList;

        countriesList.value = msg.countriesList;
        regionsList.value = msg.regionsList;
        citiesList.value = msg.citiesList;

        rowsAdd(table.value.table, prepControlUserList(table.value, msg.controlUserList), reset);
    });