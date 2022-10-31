import {initEvent} from "./place/work/initEvent";
import {validate} from "./place/form/validate";
import {placeInfo} from "../app/placeInfo";
import {init} from "./place/table/init";

(() => {

    placeInfo();

    init();

    initEvent();

    validate();
})();