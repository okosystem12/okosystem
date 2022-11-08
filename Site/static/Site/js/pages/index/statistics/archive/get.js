import {archive} from "../../../../req/index/statistics/archive";
import {fill} from './fill'

export const get = () =>
    archive((msg) =>
        fill(msg.archiveList));