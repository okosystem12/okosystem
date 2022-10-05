import {doNothing} from "../doNothing";

export const hide = (elem = null, hideCallback = doNothing) => {
    if (elem !== null) {

        elem.on('hide.bs.modal', (e) => hideCallback(e));

        elem.modal('hide');
    }
};