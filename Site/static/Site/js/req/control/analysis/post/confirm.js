import {doNothing} from "../../../../utils/doNothing";
import {main} from "../../../main";
import {userId} from "../../../../storage/control/userId";

export const confirm = (id = null, callback = doNothing) =>
     main('/control/analysis/post/confirm/', {id, userId: userId.value}, callback);