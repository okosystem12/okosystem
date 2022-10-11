import {doNothing} from "../doNothing";

export const show = (elem = null, showCallback = doNothing, hideCallback = doNothing) => {
    if (elem !== null) {

        elem.on('show.bs.modal', (e) => showCallback(e));
        elem.on('hide.bs.modal', (e) => hideCallback(e));

        elem.modal('show');
    }
};