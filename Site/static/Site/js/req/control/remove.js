import {main} from "../main";
import {doNothing} from "../../utils/doNothing";

export const remove = (data) =>
    main('/control/remove/', data, doNothing, true);