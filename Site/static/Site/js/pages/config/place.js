import {initEvent} from "./place/work/initEvent";
import {validate} from "./place/form/validate";
import {placeInfo} from "../app/placeInfo";

(() => {

    placeInfo();

    initEvent();

    validate();
})();