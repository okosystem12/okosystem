import {initEvent} from "./vch/work/initEvent";
import {validate} from "./vch/form/validate";
import {init} from "./vch/table/init";

(() => {
    init();

    initEvent();

    validate();
})();