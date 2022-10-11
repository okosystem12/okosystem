import {initFile} from "../../../utils/file/initFile";

export const upload = (elem,  uploadSuccess, fileRemove) =>
    initFile(elem, "/control/work/img/", "image/*", true, uploadSuccess, fileRemove);