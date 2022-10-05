import {countryBtnAddEvent} from "./countryBtnAddEvent";
import {regionBtnAddEvent} from "./regionBtnAddEvent";
import {cityBtnAddEvent} from "./cityBtnAddEvent";
import {placeTypeEvent} from "./placeTypeEvent";

export const initEvent = () => {
    countryBtnAddEvent();
    regionBtnAddEvent();
    cityBtnAddEvent();
    placeTypeEvent();
};