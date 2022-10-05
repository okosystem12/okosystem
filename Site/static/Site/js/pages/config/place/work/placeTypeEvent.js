import {componentsData} from "../componentsData";
import {initChosen} from "../../../../utils/list/initChosen";
import {type} from "../../../../storage/config/place/type";
import {placeInfo} from "../../../app/placeInfo";
import {btnToggleByType} from "./btnToggleByType";

export const placeTypeEvent = () => {
    const {placeType} = componentsData;
    initChosen(placeType);
    placeType.change(() => {
        type.value = placeType.val();
        placeInfo();
        btnToggleByType();
    });
};