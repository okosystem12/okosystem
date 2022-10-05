import {componentsData} from "../../pages/control/componentsData";
import {work} from "../../req/control/work";
import {rowsAdd} from "../../table/handler/rowsAdd";
import {userId} from "../../storage/control/userId";
import {removeRowById} from "../../table/handler/removeRowById";
import {controlUserList} from "../../storage/control/controlUserList";
import {controlUserImgList} from "../../storage/control/controlUserImgList";
import {fileList} from "../../storage/control/fileList";
import {mailList as mailListStorage} from "../../storage/control/mailList";
import {phoneList as phoneListStorage} from "../../storage/control/phoneList";
import {componentData} from "../../components/componentList/componentData";
import {table} from "../../storage/control/table";
import {prepControlUserList} from "../../pages/control/prepControlUserList";
import {placeList} from "../../storage/app/placeList";
import {hide} from "../../utils/modal/hide";

export const controlForm = (form, e) => {
    e.preventDefault();

    const photoList = componentsData.photoList.uploaderFileList().map(el => el.realId);
    const phoneList = componentData(componentsData.phoneList).filter(el => el.value !== '');
    const mailList = componentData(componentsData.mailList).filter(el => el.value !== '');
    const phoneIdList = phoneList.map(el => el.id);
    const mailIdList = mailList.map(el => el.id);


    work({
        id: userId.value,
        lastName: componentsData.lastName.val().trim(),
        firstName: componentsData.firstName.val().trim(),
        patronymic: componentsData.patronymic.val().trim(),
        birthDate: componentsData.birthDate.val().trim(),
        birthCountry: componentsData.birthCountry.val(),
        birthRegion: componentsData.birthRegion.val(),
        birthCity: componentsData.birthCity.val(),
        photoList,
        phoneList,
        mailList,
        phoneIdList,
        mailIdList
    }, (msg) => {
        if (msg.successText) {
            removeRowById(table.value.table,userId.value);
            controlUserList.remove('id', userId.value);
            controlUserImgList.remove('controlUser_id', userId.value);
            phoneListStorage.remove('controlUser_id', userId.value);
            mailListStorage.remove('controlUser_id', userId.value);

            controlUserList.pushList(msg.controlUserList);
            fileList.pushList(msg.fileList);
            controlUserImgList.pushList(msg.controlUserImgList);
            phoneListStorage.pushList(msg.phoneList);
            mailListStorage.pushList(msg.mailList);
            placeList.value = msg.placeList;

            rowsAdd(table.value.table, prepControlUserList(table.value, msg.controlUserList), false, false);
            hide(componentsData.controlModal);
        }
    })
};