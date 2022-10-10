import {countryBtnAddEvent} from "./countryBtnAddEvent";
import {regionBtnAddEvent} from "./regionBtnAddEvent";
import {cityBtnAddEvent} from "./cityBtnAddEvent";

export const initEvent = () => {
    countryBtnAddEvent();
    regionBtnAddEvent();
    cityBtnAddEvent();
};