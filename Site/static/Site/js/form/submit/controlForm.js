import {componentsData} from "../../pages/control/componentsData";
import {work} from "../../req/control/work";
import {userId} from "../../storage/control/userId";
import {componentData} from "../../components/componentList/componentData";
import {table} from "../../storage/control/table";
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
        schools: componentsData.schools.val().trim(),
        universities: componentsData.universities.val().trim(),
        work: componentsData.work.val().trim(),
        birthDate: componentsData.birthDate.val().trim(),
        birthCountry: componentsData.birthCountry.val(),
        birthRegion: componentsData.birthRegion.val(),
        birthCity: componentsData.birthCity.val(),
        liveCountry: componentsData.liveCountry.val(),
        liveRegion: componentsData.liveRegion.val(),
        liveCity: componentsData.liveCity.val(),
        photoList,
        phoneList,
        mailList,
        phoneIdList,
        mailIdList
    }, (msg) => {
        if (msg.successText) {
            table.value.table.ajax.reload(false);
            hide(componentsData.controlModal);
        }
    })
};