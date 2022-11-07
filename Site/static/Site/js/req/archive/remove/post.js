import {doNothing} from "../../../utils/doNothing";
import {main} from "../../main";

export const post = (data = {}, callback = doNothing) =>
    main('/archive/remove/post/', data, callback);