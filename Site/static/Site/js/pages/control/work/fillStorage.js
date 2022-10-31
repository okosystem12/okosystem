import {placeList} from "../../../storage/app/placeList";
import {mailList} from "../../../storage/control/mailList";
import {phoneList} from "../../../storage/control/phoneList";
import {fileList} from "../../../storage/control/fileList";
import {controlUserImgList} from "../../../storage/control/controlUserImgList";
import {socialList} from "../../../storage/control/socialList";
import {corruptList} from "../../../storage/control/corruptList";

export const fillStorage = (data) => {
    placeList.value = data.placeList;
    mailList.value = data.mailList;
    phoneList.value = data.phoneList;
    fileList.value = data.fileList;
    controlUserImgList.value = data.controlUserImgList;
    socialList.value = data.socialList;
    corruptList.value = data.corruptList;
};