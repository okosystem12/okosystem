import {userId} from "../../../../storage/control/userId";
import {openForm} from "../../form/openForm";
import {get} from "../../../../req/control/get";
import {placeList} from "../../../../storage/app/placeList";
import {mailList} from "../../../../storage/control/mailList";
import {phoneList} from "../../../../storage/control/phoneList";
import {fileList} from "../../../../storage/control/fileList";
import {controlUserImgList} from "../../../../storage/control/controlUserImgList";

export const edit = (id) => {
    userId.value = parseInt(id);

    get({id: userId.value}, (msg) => {
        placeList.value = msg.placeList;
        mailList.value = msg.mailList;
        phoneList.value = msg.phoneList;
        fileList.value = msg.fileList;
        controlUserImgList.value = msg.controlUserImgList;
        openForm(msg.user[0]);
    })
};