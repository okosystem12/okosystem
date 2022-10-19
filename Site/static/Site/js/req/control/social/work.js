import {main} from "../../main";
import {userId} from "../../../storage/control/userId";

export const work = (data, callback) =>
    main('/control/social/work/', {...data, userId: userId.value}, callback);