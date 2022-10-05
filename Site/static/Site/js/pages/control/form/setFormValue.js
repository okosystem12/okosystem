import {bDate} from "../../../utils/date/bDate";
import {fileList} from "../../../storage/control/fileList";
import {controlUserImgList} from "../../../storage/control/controlUserImgList";
import {prepUri} from "../../../utils/file/prepUri";
import {phoneList as storagePhoneList} from "../../../storage/control/phoneList";
import {mailList as storageMailList} from "../../../storage/control/mailList";
import {componentList} from "../../../components/componentList/componentList";
import {initOptionList} from "../../../components/select/initOptionList";
import {countriesList} from "../../../storage/app/countriesList";
import {emptyControlForm} from "./emptyControlForm";
import {componentsData} from "../componentsData";
import {filterRegion} from "../../../utils/list/filter/filterRegion";
import {filterCities} from "../../../utils/list/filter/filterCities";
import {placeList} from "../../../storage/app/placeList";
import {label} from "../../../utils/modal/label";
import {userId} from "../../../storage/control/userId";


export const setFormValue = (data = emptyControlForm) => {
    const defaultFileList = [];

    const {
        controlModalLabel,
        lastName,
        firstName,
        patronymic,
        birthDate,
        photoList,
        phoneList,
        mailList,
        birthCountry,
        birthRegion,
        birthCity,
    } = componentsData;

    userId.value = data.id || null;

    label(controlModalLabel, userId.value, '', data.lastName);

    lastName.val(data.lastName);
    firstName.val(data.firstName);
    patronymic.val(data.patronymic);
    birthDate.datepicker("setDate", bDate(data));

    photoList.uploaderClean();

    controlUserImgList.value.filter(el => el.controlUser_id === data.id).forEach(el => {
        const file = fileList.value.find(f => f.id === el.file_id);

        if (file) {
            defaultFileList.push({
                realId: file.id,
                name: file.name,
                url: prepUri(file.file)
            })
        }
    });

    photoList.uploaderDefaultFiles(defaultFileList);

    componentList(phoneList, storagePhoneList.value.filter(el => el.controlUser_id === data.id));
    componentList(mailList, storageMailList.value.filter(el => el.controlUser_id === data.id));


    placeEngine(birthCountry, birthRegion, birthCity, data.birthPlace_id)

};

const placeEngine = (country, region, city, place_id = null) => {
    const place = placeList.value.find(el => el.id === place_id);

    initOptionList(country, countriesList.value, place?.country_id || '');
    initOptionList(region, filterRegion(parseInt(country.val())),  place?.region_id || '');
    initOptionList(city, filterCities(parseInt(country.val()), parseInt(city.val())),  place?.city_id || '');

    country.unbind('change').change(() => {
        initOptionList(region, filterRegion(parseInt(country.val())), '');
        initOptionList(city, filterCities(parseInt(country.val())), '');
    });

    region.unbind('change').change(() => {
        initOptionList(city, filterCities(parseInt(country.val()), parseInt(city.val())), '');
    })
};



