import {initEvent} from "./vch/work/initEvent";
import {vchForm} from "../../form/validate/vchForm";
import {init} from "./vch/table/init";

(() => {
    init();

    initEvent();

    vchForm();
})();