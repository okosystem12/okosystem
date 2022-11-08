import {controlUser} from "../../../../req/index/statistics/controlUser";
import {fill} from './fill'

export const get = () =>
    controlUser((msg) =>
        fill(msg.controlUserList));