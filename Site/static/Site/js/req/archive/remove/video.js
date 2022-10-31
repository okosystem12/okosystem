import {doNothing} from "../../../utils/doNothing";
import {main} from "../../main";

export const video = (data = {}, callback = doNothing) =>
    main('/archive/remove/video/', data, callback, true);