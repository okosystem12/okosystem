import {initEvent} from "./vch/work/initEvent";
import {vchForm} from "../../form/validate/vchForm";
import {vchInfo} from "../app/vchInfo";

(() => {
    vchInfo();

    initEvent();

    vchForm();
})();