import {responseConverter} from "./responseConverter";
import {paramsBuilder} from "./paramsBuilder";
import {ajaxRequester} from "./ajaxRequester";

export const initFile = (elem, url, accept, multiple, uploadSuccess, fileRemove) =>
    elem.uploader({
        multiple,
        accept,
        ajaxConfig: {
            url: url,
            method: "post",
            paramsBuilder: paramsBuilder,
            ajaxRequester: ajaxRequester,
            responseConverter: responseConverter,
        },
    }).on("upload-success", uploadSuccess).on("file-remove", fileRemove);

