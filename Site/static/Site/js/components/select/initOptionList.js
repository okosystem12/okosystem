import {optionList} from "./optionList";
import {initChosen} from "../../utils/list/initChosen";

export const initOptionList = (place, list = [], value = null) => {
    const old = place.val();
    place.html(optionList(list));
    place.val(value);
    initChosen(place);
};