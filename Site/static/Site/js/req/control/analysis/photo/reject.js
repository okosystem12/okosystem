import {doNothing} from "../../../../utils/doNothing";
import {main} from "../../../main";
import {userId} from "../../../../storage/control/userId";

export const reject = (id = null, callback = doNothing) =>
     main('/control/analysis/photo/reject/', {id, userId: userId.value}, callback);