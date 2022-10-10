import {initDatepickerPast} from "../../../utils/date/initDatepickerPast";
import {initChosen} from "../../../utils/list/initChosen";
import {componentsData} from "../componentsData";
import {upload} from "../../../req/control/file/upload";
import {remove} from "../../../req/control/file/remove";
import {userId} from "../../../storage/control/userId";
import {controlUserImgList} from "../../../storage/control/controlUserImgList";

export const prepControlForm = () => {
    const {
        birthCity, birthCountry, birthRegion,
        liveCity, liveCountry, liveRegion,
        birthDate,  photoList} = componentsData;

    initDatepickerPast(birthDate);

    initChosen(birthCity);
    initChosen(birthCountry);
    initChosen(birthRegion);

    initChosen(liveCity);
    initChosen(liveCountry);
    initChosen(liveRegion);

    upload(photoList, (e, file) => {
    }, (e, file) => {
        remove({
            controlUserId: userId.value,
            id: [file.realId]
        });

        controlUserImgList.remove('file_id', file.realId);
    });
};