import {responseConverter} from "../../req/file/responseConverter";
import {paramsBuilder} from "../../req/file/paramsBuilder";
import {ajaxRequester} from "../../req/file/ajaxRequester";
import {doNothing} from "../doNothing";

export const initFile = (elem = null, url = '', accept = '', multiple = false, uploadSuccess = doNothing, fileRemove = doNothing) => {
    if (elem !== null) {
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
    }
}
