import {doNothing} from "../../../utils/doNothing";
import {main} from "../../main";
import {userId} from "../../../storage/control/userId";

export const add = (value = '', callback = doNothing) =>
    main('/control/social/add/', {value, userId: userId.value}, callback);